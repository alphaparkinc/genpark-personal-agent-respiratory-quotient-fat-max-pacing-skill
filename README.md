# Respiratory Exchange Ratio (RER) & FatMax Pacing Sentinel Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Substrate oxidation ratio (fat vs carb kcal/min) from respiratory exchange ratio (RER/RQ), FatMax training zone, and metabolic flexibility score. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_substrate_oxidation_rates`: Calculate grams and percentages of fat vs carbohydrate oxidation from VO2 (L/min) and VCO2 (L/min).
- `identify_fatmax_endurance_power_zone`: Identify watt / pace sweet-spot for maximum grams per hour of lipid oxidation to spare glycogen.

## 🚀 Installation & Usage
```bash
python -m genpark_personal_agent_respiratory_quotient_fat_max_pacing_skill.server --test
```
