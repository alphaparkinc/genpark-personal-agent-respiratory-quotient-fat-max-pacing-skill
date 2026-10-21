# -*- coding: utf-8 -*-
"""Respiratory Exchange Ratio & FatMax Sentinel for GenPark Personal Agent."""
import json
from typing import Dict, Any

class RespiratoryExchangeRatioFatMaxSentinel:
    @staticmethod
    def calculate_substrate_oxidation_rates(vo2_liters_min: float, vco2_liters_min: float) -> Dict[str, Any]:
        rer = round(vco2_liters_min / max(0.1, vo2_liters_min), 3)
        # Frayn stoichiometric equations:
        # Fat oxidation (g/min) = 1.67 * VO2 - 1.67 * VCO2
        # CHO oxidation (g/min) = 4.55 * VCO2 - 3.21 * VO2
        fat_g_min = round(max(0.0, 1.67 * vo2_liters_min - 1.67 * vco2_liters_min), 2)
        cho_g_min = round(max(0.0, 4.55 * vco2_liters_min - 3.21 * vo2_liters_min), 2)
        
        fat_kcal_min = round(fat_g_min * 9.0, 1)
        cho_kcal_min = round(cho_g_min * 4.0, 1)
        total_kcal_min = round(fat_kcal_min + cho_kcal_min, 1)
        
        fat_contrib_pct = round((fat_kcal_min / max(0.1, total_kcal_min)) * 100.0, 1)
        
        return {
            "rer": rer,
            "fat_oxidation_g_min": fat_g_min,
            "carb_oxidation_g_min": cho_g_min,
            "fat_kcal_hr": round(fat_kcal_min * 60.0, 0),
            "carb_kcal_hr": round(cho_kcal_min * 60.0, 0),
            "fat_caloric_contribution_pct": fat_contrib_pct,
            "metabolic_fuel_predominance": "LIPID_OXIDATION (Glycogen Sparing)" if rer <= 0.85 else "CARBOHYDRATE_GLYCOLYSIS"
        }

    @staticmethod
    def identify_fatmax_endurance_power_zone(peak_fat_oxidation_watts: int, ftp_watts: int) -> Dict[str, Any]:
        pct_ftp = round((peak_fat_oxidation_watts / max(1, ftp_watts)) * 100.0, 1)
        zone_low = int(peak_fat_oxidation_watts * 0.92)
        zone_high = int(peak_fat_oxidation_watts * 1.05)
        
        return {
            "fatmax_watts": peak_fat_oxidation_watts,
            "fatmax_pct_of_ftp": pct_ftp,
            "optimal_aerobic_target_power_window": f"{zone_low}W - {zone_high}W",
            "race_pacing_strategy": "Maintain this wattage on flats to preserve hepatic and muscular glycogen reserves for final climbs."
        }
