async def dynamic_congestion_optimize_service(weights: dict) -> dict:
    """
    1. Normaliza la suma de los pesos para que sea 1.
    2. Calcula baseline y optimized con fórmulas lineales+cuadráticas.
    3. Calcula difference como (baseline-optimized)/baseline.
    4. Renombra métricas y excluye PT Frequency/System Cost.
    5. Trunca todos los valores a 2 decimales.
    """
    # 1) Normalizar pesos
    total = sum(weights.values())
    if total != 1:
        weights = {k: v / total for k, v in weights.items()}

    # 2) Extraer pesos
    w_pt = weights["weight_PublicTransport"]
    w_cong = weights["weight_Congestion"]
    w_oc = weights["weight_OperationalCost"]
    w_em = weights["weight_Emissions"]

    # 3) Cálculo baseline y optimized
    baseline = {
        "Income": w_oc * 0.3 + (w_oc ** 2) * 0.1,
        "Congestion inside": w_pt * 400 + (w_pt ** 2) * 50,
        "Congestion (Delay)": w_cong * 0.8 + (w_cong ** 2) * 0.1,
        "Emissions": w_em * 0.007 + (w_em ** 2) * 0.001,
    }
    optimized = {
        "Income": w_oc * 0.4 + (w_oc ** 2) * 0.12,
        "Congestion inside": w_pt * 360 + (w_pt ** 2) * 40,
        "Congestion (Delay)": w_cong * 1.0 + (w_cong ** 2) * 0.15,
        "Emissions": w_em * 0.07 + (w_em ** 2) * 0.008,
    }

    # 4) Cálculo differences
    difference = {}
    for key in ["Income", "Congestion inside", "Congestion (Delay)", "Emissions"]:
        base_val = baseline[key]
        opt_val = optimized[key]
        difference[key] = (base_val - opt_val) / base_val if base_val else 0

    # 5) Truncar todos los valores a 2 decimales
    baseline = {k: round(v, 2) for k, v in baseline.items()}
    optimized = {k: round(v, 2) for k, v in optimized.items()}
    difference = {k: round(v, 2) for k, v in difference.items()}

    return {"baseline": baseline,
            "optimized": optimized,
            "difference": difference}
