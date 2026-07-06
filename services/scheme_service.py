import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# ==========================================
# Gemini Configuration
# ==========================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=GEMINI_API_KEY
)

# ==========================================
# Government Schemes Database
# ==========================================
SCHEMES = {

    "Maharashtra": {

        "Small Farmer": [
            {
                "name": "PM Kisan Samman Nidhi",
                "description": "Income support of ₹6000 per year.",
                "eligibility": "Small farmers owning cultivable land.",
                "benefits": "₹6000 annual financial assistance."
            },
            {
                "name": "PM Fasal Bima Yojana",
                "description": "Crop insurance against natural calamities.",
                "eligibility": "Small farmers growing notified crops.",
                "benefits": "Insurance for crop losses."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Low-interest agricultural loan.",
                "eligibility": "Small farmers.",
                "benefits": "Easy crop loans at subsidized interest."
            },
            {
                "name": "Soil Health Card",
                "description": "Free soil testing service.",
                "eligibility": "All farmers.",
                "benefits": "Scientific fertilizer recommendations."
            },
            {
                "name": "Mahatma Jyotiba Phule Karj Mukti Yojana",
                "description": "Loan waiver assistance.",
                "eligibility": "Eligible Maharashtra farmers.",
                "benefits": "Relief from agricultural loans."
            }
        ],

        "Marginal Farmer": [
            {
                "name": "PM Kisan Samman Nidhi",
                "description": "Direct income support.",
                "eligibility": "Marginal farmers.",
                "benefits": "₹6000 yearly."
            },
            {
                "name": "PMFBY",
                "description": "Crop insurance.",
                "eligibility": "Marginal farmers.",
                "benefits": "Compensation for crop damage."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Agricultural credit.",
                "eligibility": "Marginal farmers.",
                "benefits": "Working capital."
            },
            {
                "name": "National Food Security Mission",
                "description": "Increase food grain production.",
                "eligibility": "Marginal farmers.",
                "benefits": "Seed and fertilizer assistance."
            },
            {
                "name": "Soil Health Card",
                "description": "Soil analysis.",
                "eligibility": "All farmers.",
                "benefits": "Improved soil fertility."
            }
        ],

        "Medium Farmer": [
            {
                "name": "PM Kisan",
                "description": "Income support.",
                "eligibility": "Eligible farmers.",
                "benefits": "₹6000 annually."
            },
            {
                "name": "PMFBY",
                "description": "Crop insurance.",
                "eligibility": "Medium farmers.",
                "benefits": "Crop protection."
            },
            {
                "name": "Agricultural Mechanization Scheme",
                "description": "Subsidy for farm machinery.",
                "eligibility": "Medium farmers.",
                "benefits": "Equipment subsidy."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Farm loans.",
                "eligibility": "Medium farmers.",
                "benefits": "Low-interest credit."
            },
            {
                "name": "Soil Health Card",
                "description": "Soil testing.",
                "eligibility": "All farmers.",
                "benefits": "Better nutrient management."
            }
        ],

        "Large Farmer": [
            {
                "name": "Agricultural Infrastructure Fund",
                "description": "Infrastructure financing.",
                "eligibility": "Large farmers.",
                "benefits": "Investment support."
            },
            {
                "name": "PMFBY",
                "description": "Crop insurance.",
                "eligibility": "Large farmers.",
                "benefits": "Insurance cover."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Agricultural finance.",
                "eligibility": "Large farmers.",
                "benefits": "Higher loan limit."
            },
            {
                "name": "Farm Mechanization Scheme",
                "description": "Modern machinery subsidy.",
                "eligibility": "Large farmers.",
                "benefits": "Advanced farm equipment."
            },
            {
                "name": "Micro Irrigation Fund",
                "description": "Support for drip irrigation.",
                "eligibility": "Large farmers.",
                "benefits": "Water-saving subsidy."
            }
        ]
    },

    "Karnataka": {

        "Small Farmer": [
            {
                "name": "Raitha Siri",
                "description": "Support for millet cultivation.",
                "eligibility": "Small millet farmers.",
                "benefits": "Financial assistance."
            },
            {
                "name": "PM Kisan",
                "description": "Income support.",
                "eligibility": "Small farmers.",
                "benefits": "₹6000 annually."
            },
            {
                "name": "PMFBY",
                "description": "Crop insurance.",
                "eligibility": "Small farmers.",
                "benefits": "Insurance cover."
            },
            {
                "name": "Bhoochetana",
                "description": "Soil health improvement.",
                "eligibility": "Farmers.",
                "benefits": "Higher productivity."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Farm loan.",
                "eligibility": "Small farmers.",
                "benefits": "Easy finance."
            }
        ],

        "Marginal Farmer": [
            {
                "name": "PM Kisan",
                "description": "Income support.",
                "eligibility": "Marginal farmers.",
                "benefits": "₹6000 annually."
            },
            {
                "name": "PMFBY",
                "description": "Insurance.",
                "eligibility": "Marginal farmers.",
                "benefits": "Crop loss protection."
            },
            {
                "name": "Raitha Siri",
                "description": "Millet support.",
                "eligibility": "Marginal farmers.",
                "benefits": "Production incentive."
            },
            {
                "name": "Soil Health Card",
                "description": "Free soil testing.",
                "eligibility": "Farmers.",
                "benefits": "Balanced fertilizer usage."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Agricultural loans.",
                "eligibility": "Marginal farmers.",
                "benefits": "Working capital."
            }
        ],

        "Medium Farmer": [
            {
                "name": "PMFBY",
                "description": "Crop insurance.",
                "eligibility": "Medium farmers.",
                "benefits": "Risk coverage."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Farm finance.",
                "eligibility": "Medium farmers.",
                "benefits": "Low-interest loans."
            },
            {
                "name": "Agricultural Mechanization Scheme",
                "description": "Machinery subsidy.",
                "eligibility": "Medium farmers.",
                "benefits": "Equipment support."
            },
            {
                "name": "Bhoochetana",
                "description": "Soil improvement.",
                "eligibility": "Farmers.",
                "benefits": "Higher yield."
            },
            {
                "name": "PM Kisan",
                "description": "Income support.",
                "eligibility": "Eligible farmers.",
                "benefits": "₹6000 annually."
            }
        ],

        "Large Farmer": [
            {
                "name": "Agricultural Infrastructure Fund",
                "description": "Infrastructure loan.",
                "eligibility": "Large farmers.",
                "benefits": "Capital investment."
            },
            {
                "name": "Farm Mechanization",
                "description": "Equipment subsidy.",
                "eligibility": "Large farmers.",
                "benefits": "Modern machinery."
            },
            {
                "name": "Micro Irrigation Fund",
                "description": "Drip irrigation support.",
                "eligibility": "Large farmers.",
                "benefits": "Water conservation."
            },
            {
                "name": "PMFBY",
                "description": "Insurance.",
                "eligibility": "Large farmers.",
                "benefits": "Crop protection."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Agricultural loans.",
                "eligibility": "Large farmers.",
                "benefits": "Higher credit limit."
            }
        ]
    },

    "Kerala": {

        "Small Farmer": [
            {
                "name": "PM Kisan",
                "description": "Income support.",
                "eligibility": "Small farmers.",
                "benefits": "₹6000 annually."
            },
            {
                "name": "PMFBY",
                "description": "Crop insurance.",
                "eligibility": "Small farmers.",
                "benefits": "Insurance coverage."
            },
            {
                "name": "Vegetable Promotion Programme",
                "description": "Promotes vegetable farming.",
                "eligibility": "Small vegetable growers.",
                "benefits": "Subsidy and technical guidance."
            },
            {
                "name": "Soil Health Card",
                "description": "Free soil testing.",
                "eligibility": "All farmers.",
                "benefits": "Scientific nutrient advice."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Agricultural loan.",
                "eligibility": "Small farmers.",
                "benefits": "Easy finance."
            }
        ],

        "Marginal Farmer": [
            {
                "name": "PM Kisan",
                "description": "Income support.",
                "eligibility": "Marginal farmers.",
                "benefits": "₹6000 annually."
            },
            {
                "name": "PMFBY",
                "description": "Crop insurance.",
                "eligibility": "Marginal farmers.",
                "benefits": "Risk protection."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Farm loans.",
                "eligibility": "Marginal farmers.",
                "benefits": "Working capital."
            },
            {
                "name": "Vegetable Promotion Programme",
                "description": "Vegetable cultivation support.",
                "eligibility": "Marginal farmers.",
                "benefits": "Production assistance."
            },
            {
                "name": "Soil Health Card",
                "description": "Soil testing.",
                "eligibility": "Farmers.",
                "benefits": "Better fertilizer management."
            }
        ],

        "Medium Farmer": [
            {
                "name": "PMFBY",
                "description": "Crop insurance.",
                "eligibility": "Medium farmers.",
                "benefits": "Insurance."
            },
            {
                "name": "Agricultural Mechanization",
                "description": "Machinery subsidy.",
                "eligibility": "Medium farmers.",
                "benefits": "Modern equipment."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Farm finance.",
                "eligibility": "Medium farmers.",
                "benefits": "Easy credit."
            },
            {
                "name": "PM Kisan",
                "description": "Income support.",
                "eligibility": "Eligible farmers.",
                "benefits": "₹6000 annually."
            },
            {
                "name": "Soil Health Card",
                "description": "Soil testing.",
                "eligibility": "Farmers.",
                "benefits": "Balanced nutrients."
            }
        ],

        "Large Farmer": [
            {
                "name": "Agricultural Infrastructure Fund",
                "description": "Infrastructure investment.",
                "eligibility": "Large farmers.",
                "benefits": "Financial support."
            },
            {
                "name": "Micro Irrigation Fund",
                "description": "Drip irrigation assistance.",
                "eligibility": "Large farmers.",
                "benefits": "Water-saving subsidy."
            },
            {
                "name": "Farm Mechanization",
                "description": "Equipment subsidy.",
                "eligibility": "Large farmers.",
                "benefits": "Modern machinery."
            },
            {
                "name": "PMFBY",
                "description": "Crop insurance.",
                "eligibility": "Large farmers.",
                "benefits": "Crop protection."
            },
            {
                "name": "Kisan Credit Card",
                "description": "Agricultural finance.",
                "eligibility": "Large farmers.",
                "benefits": "High-value loans."
            }
        ]
    }


,
"Tamil Nadu": {

    "Small Farmer": [

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Direct income support to eligible farmers.",
            "eligibility": "Small farmers with cultivable land.",
            "benefits": "₹6000 per year in three installments."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance against natural disasters.",
            "eligibility": "Small farmers growing notified crops.",
            "benefits": "Compensation for crop losses."
        },

        {
            "name": "Tamil Nadu Agricultural Mechanization Scheme",
            "description": "Subsidy for purchasing agricultural machinery.",
            "eligibility": "Small farmers.",
            "benefits": "40–50% subsidy on farm equipment."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Promotes drip and sprinkler irrigation.",
            "eligibility": "Farmers with irrigated land.",
            "benefits": "Up to 55% subsidy."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Short-term agricultural loans.",
            "eligibility": "Small farmers.",
            "benefits": "Low-interest crop loans."
        }

    ],

    "Marginal Farmer": [

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Financial support for farmers.",
            "eligibility": "Marginal farmers.",
            "benefits": "₹6000 annual assistance."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Insurance against crop failure.",
            "eligibility": "Marginal farmers.",
            "benefits": "Financial protection."
        },

        {
            "name": "Soil Health Card",
            "description": "Scientific soil testing.",
            "eligibility": "All farmers.",
            "benefits": "Better fertilizer recommendations."
        },

        {
            "name": "Tamil Nadu Seed Distribution Scheme",
            "description": "Subsidized certified seeds.",
            "eligibility": "Marginal farmers.",
            "benefits": "Improved crop productivity."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural credit support.",
            "eligibility": "Marginal farmers.",
            "benefits": "Easy crop loans."
        }

    ],

    "Medium Farmer": [

        {
            "name": "Agricultural Mechanization Scheme",
            "description": "Support for modern farming equipment.",
            "eligibility": "Medium farmers.",
            "benefits": "Machinery subsidy."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Medium farmers.",
            "benefits": "Insurance against losses."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Efficient irrigation support.",
            "eligibility": "Medium farmers.",
            "benefits": "Subsidy for drip irrigation."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Farm credit.",
            "eligibility": "Medium farmers.",
            "benefits": "Low-interest loans."
        },

        {
            "name": "Soil Health Card",
            "description": "Free soil testing.",
            "eligibility": "All farmers.",
            "benefits": "Balanced fertilizer usage."
        }

    ],

    "Large Farmer": [

        {
            "name": "Agricultural Infrastructure Fund",
            "description": "Financial assistance for farm infrastructure.",
            "eligibility": "Large farmers.",
            "benefits": "Long-term investment support."
        },

        {
            "name": "Farm Mechanization Scheme",
            "description": "Modern agricultural machinery.",
            "eligibility": "Large farmers.",
            "benefits": "Subsidy on advanced equipment."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Water-saving irrigation.",
            "eligibility": "Large farmers.",
            "benefits": "Subsidy for irrigation systems."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Large farmers.",
            "benefits": "Protection against crop loss."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural finance.",
            "eligibility": "Large farmers.",
            "benefits": "Higher credit limits."
        }

    ]

}

,
"Andhra Pradesh": {

    "Small Farmer": [

        {
            "name": "YSR Rythu Bharosa",
            "description": "Financial assistance to eligible farmers.",
            "eligibility": "Small farmers in Andhra Pradesh.",
            "benefits": "Annual financial support for cultivation."
        },

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Income support for farmers.",
            "eligibility": "Eligible small farmers.",
            "benefits": "₹6000 per year."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance against natural calamities.",
            "eligibility": "Farmers growing notified crops.",
            "benefits": "Compensation for crop loss."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Short-term agricultural loans.",
            "eligibility": "Small farmers.",
            "benefits": "Low-interest farm loans."
        },

        {
            "name": "Soil Health Card",
            "description": "Free soil testing and nutrient analysis.",
            "eligibility": "All farmers.",
            "benefits": "Better fertilizer management."
        }

    ],

    "Marginal Farmer": [

        {
            "name": "YSR Rythu Bharosa",
            "description": "Income support for marginal farmers.",
            "eligibility": "Marginal farmers.",
            "benefits": "Annual financial assistance."
        },

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Direct income support.",
            "eligibility": "Marginal farmers.",
            "benefits": "₹6000 yearly."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance scheme.",
            "eligibility": "Marginal farmers.",
            "benefits": "Protection from crop failure."
        },

        {
            "name": "Seed Distribution Scheme",
            "description": "Certified seed distribution.",
            "eligibility": "Marginal farmers.",
            "benefits": "Quality seeds at subsidized rates."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural credit support.",
            "eligibility": "Marginal farmers.",
            "benefits": "Easy crop loans."
        }

    ],

    "Medium Farmer": [

        {
            "name": "Agricultural Mechanization Scheme",
            "description": "Subsidy for farm machinery.",
            "eligibility": "Medium farmers.",
            "benefits": "Modern agricultural equipment."
        },

        {
            "name": "YSR Rythu Bharosa",
            "description": "Farmer financial assistance.",
            "eligibility": "Medium farmers.",
            "benefits": "Income support."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Medium farmers.",
            "benefits": "Risk protection."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Support for drip irrigation.",
            "eligibility": "Medium farmers.",
            "benefits": "Water conservation subsidy."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural finance.",
            "eligibility": "Medium farmers.",
            "benefits": "Low-interest loans."
        }

    ],

    "Large Farmer": [

        {
            "name": "Agricultural Infrastructure Fund",
            "description": "Infrastructure financing.",
            "eligibility": "Large farmers.",
            "benefits": "Financial support for warehouses and cold storage."
        },

        {
            "name": "Farm Mechanization Scheme",
            "description": "Modern machinery subsidy.",
            "eligibility": "Large farmers.",
            "benefits": "Advanced farm equipment."
        },

        {
            "name": "YSR Rythu Bharosa",
            "description": "State financial assistance.",
            "eligibility": "Eligible farmers.",
            "benefits": "Annual support."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Large farmers.",
            "benefits": "Insurance against crop damage."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Drip and sprinkler irrigation.",
            "eligibility": "Large farmers.",
            "benefits": "Subsidy for efficient irrigation."
        }

    ]

}

,
"Telangana": {

    "Small Farmer": [

        {
            "name": "Rythu Bandhu Scheme",
            "description": "Investment support for farmers before every crop season.",
            "eligibility": "Small farmers owning agricultural land.",
            "benefits": "Financial assistance for purchasing seeds, fertilizers and other farm inputs."
        },

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Income support for eligible farmers.",
            "eligibility": "Small farmers.",
            "benefits": "₹6000 per year in three installments."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance against natural calamities.",
            "eligibility": "Farmers cultivating notified crops.",
            "benefits": "Insurance coverage for crop losses."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Short-term agricultural credit.",
            "eligibility": "Small farmers.",
            "benefits": "Low-interest crop loans."
        },

        {
            "name": "Soil Health Card",
            "description": "Scientific soil testing service.",
            "eligibility": "All farmers.",
            "benefits": "Improves fertilizer management and crop productivity."
        }

    ],

    "Marginal Farmer": [

        {
            "name": "Rythu Bandhu Scheme",
            "description": "Investment assistance for cultivation.",
            "eligibility": "Marginal farmers.",
            "benefits": "Financial support before every crop season."
        },

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Direct income support.",
            "eligibility": "Marginal farmers.",
            "benefits": "₹6000 yearly."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance scheme.",
            "eligibility": "Marginal farmers.",
            "benefits": "Protection against crop failure."
        },

        {
            "name": "Seed Distribution Scheme",
            "description": "Distribution of certified seeds.",
            "eligibility": "Marginal farmers.",
            "benefits": "Subsidized quality seeds."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural finance.",
            "eligibility": "Marginal farmers.",
            "benefits": "Easy crop loans."
        }

    ],

    "Medium Farmer": [

        {
            "name": "Rythu Bandhu Scheme",
            "description": "Seasonal investment support.",
            "eligibility": "Medium farmers.",
            "benefits": "Financial assistance for farming operations."
        },

        {
            "name": "Agricultural Mechanization Scheme",
            "description": "Subsidy for modern agricultural machinery.",
            "eligibility": "Medium farmers.",
            "benefits": "Reduced machinery cost."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance coverage.",
            "eligibility": "Medium farmers.",
            "benefits": "Protection against natural disasters."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Support for drip and sprinkler irrigation.",
            "eligibility": "Medium farmers.",
            "benefits": "Water-saving subsidy."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural loan facility.",
            "eligibility": "Medium farmers.",
            "benefits": "Low-interest farm credit."
        }

    ],

    "Large Farmer": [

        {
            "name": "Agricultural Infrastructure Fund",
            "description": "Financial assistance for agricultural infrastructure.",
            "eligibility": "Large farmers.",
            "benefits": "Support for warehouses, storage and processing units."
        },

        {
            "name": "Rythu Bandhu Scheme",
            "description": "Investment support for cultivation.",
            "eligibility": "Eligible land-owning farmers.",
            "benefits": "Seasonal financial assistance."
        },

        {
            "name": "Farm Mechanization Scheme",
            "description": "Support for advanced farm machinery.",
            "eligibility": "Large farmers.",
            "benefits": "Subsidy on tractors and agricultural equipment."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance scheme.",
            "eligibility": "Large farmers.",
            "benefits": "Insurance against crop damage."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Drip and sprinkler irrigation support.",
            "eligibility": "Large farmers.",
            "benefits": "Subsidy for efficient irrigation systems."
        }

    ]

}
,
"Gujarat": {

    "Small Farmer": [

        {
            "name": "IKhedut Portal Scheme",
            "description": "Provides subsidies for agriculture equipment, seeds and irrigation.",
            "eligibility": "Small farmers of Gujarat.",
            "benefits": "Subsidy on farm implements and agricultural inputs."
        },

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Direct income support.",
            "eligibility": "Eligible small farmers.",
            "benefits": "₹6000 annually."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance against natural disasters.",
            "eligibility": "Farmers growing notified crops.",
            "benefits": "Financial compensation for crop loss."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural credit facility.",
            "eligibility": "Small farmers.",
            "benefits": "Low-interest crop loans."
        },

        {
            "name": "Soil Health Card",
            "description": "Free soil testing service.",
            "eligibility": "All farmers.",
            "benefits": "Improves fertilizer management."
        }

    ],

    "Marginal Farmer": [

        {
            "name": "IKhedut Portal Scheme",
            "description": "Agricultural subsidy program.",
            "eligibility": "Marginal farmers.",
            "benefits": "Financial support for farm equipment."
        },

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Income support.",
            "eligibility": "Marginal farmers.",
            "benefits": "₹6000 annually."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Marginal farmers.",
            "benefits": "Protection against crop failure."
        },

        {
            "name": "Seed Distribution Scheme",
            "description": "Certified seed assistance.",
            "eligibility": "Marginal farmers.",
            "benefits": "Subsidized quality seeds."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural finance.",
            "eligibility": "Marginal farmers.",
            "benefits": "Easy crop loans."
        }

    ],

    "Medium Farmer": [

        {
            "name": "IKhedut Portal Scheme",
            "description": "Government agricultural subsidy.",
            "eligibility": "Medium farmers.",
            "benefits": "Support for machinery and irrigation."
        },

        {
            "name": "Agricultural Mechanization Scheme",
            "description": "Farm machinery subsidy.",
            "eligibility": "Medium farmers.",
            "benefits": "Reduced machinery cost."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Medium farmers.",
            "benefits": "Insurance against crop losses."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Support for drip irrigation.",
            "eligibility": "Medium farmers.",
            "benefits": "Water-saving subsidy."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural loans.",
            "eligibility": "Medium farmers.",
            "benefits": "Low-interest finance."
        }

    ],

    "Large Farmer": [

        {
            "name": "Agricultural Infrastructure Fund",
            "description": "Infrastructure financing for agriculture.",
            "eligibility": "Large farmers.",
            "benefits": "Support for warehouses and cold storage."
        },

        {
            "name": "IKhedut Portal Scheme",
            "description": "Financial support for advanced farming.",
            "eligibility": "Large farmers.",
            "benefits": "Subsidy on high-value agricultural equipment."
        },

        {
            "name": "Farm Mechanization Scheme",
            "description": "Support for modern agricultural machinery.",
            "eligibility": "Large farmers.",
            "benefits": "Advanced equipment subsidy."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Large farmers.",
            "benefits": "Financial protection against crop damage."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Drip and sprinkler irrigation support.",
            "eligibility": "Large farmers.",
            "benefits": "Subsidy for efficient irrigation systems."
        }

    ]

}
,
"Rajasthan": {

    "Small Farmer": [

        {
            "name": "Mukhyamantri Krishak Saathi Yojana",
            "description": "Financial assistance to farmers affected by accidents during farming activities.",
            "eligibility": "Small farmers of Rajasthan.",
            "benefits": "Compensation up to ₹2 lakh."
        },

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Direct income support.",
            "eligibility": "Eligible small farmers.",
            "benefits": "₹6000 annually."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Insurance against crop loss.",
            "eligibility": "Farmers cultivating notified crops.",
            "benefits": "Compensation for natural calamities."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Short-term agricultural loans.",
            "eligibility": "Small farmers.",
            "benefits": "Low-interest crop loans."
        },

        {
            "name": "Soil Health Card",
            "description": "Free soil testing service.",
            "eligibility": "All farmers.",
            "benefits": "Improves fertilizer management."
        }

    ],

    "Marginal Farmer": [

        {
            "name": "Mukhyamantri Krishak Saathi Yojana",
            "description": "Farmer welfare scheme.",
            "eligibility": "Marginal farmers.",
            "benefits": "Financial security during emergencies."
        },

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Income support.",
            "eligibility": "Marginal farmers.",
            "benefits": "₹6000 annually."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Marginal farmers.",
            "benefits": "Insurance protection."
        },

        {
            "name": "Seed Mini Kit Scheme",
            "description": "Distribution of certified seeds.",
            "eligibility": "Marginal farmers.",
            "benefits": "Improved seed quality."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural finance.",
            "eligibility": "Marginal farmers.",
            "benefits": "Easy farm credit."
        }

    ],

    "Medium Farmer": [

        {
            "name": "Agricultural Mechanization Scheme",
            "description": "Subsidy for modern farm machinery.",
            "eligibility": "Medium farmers.",
            "benefits": "Reduced machinery cost."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Medium farmers.",
            "benefits": "Protection against crop failure."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Support for drip and sprinkler irrigation.",
            "eligibility": "Medium farmers.",
            "benefits": "Water conservation subsidy."
        },

        {
            "name": "Mukhyamantri Krishak Saathi Yojana",
            "description": "Farmer welfare assistance.",
            "eligibility": "Medium farmers.",
            "benefits": "Financial support."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural loans.",
            "eligibility": "Medium farmers.",
            "benefits": "Low-interest finance."
        }

    ],

    "Large Farmer": [

        {
            "name": "Agricultural Infrastructure Fund",
            "description": "Financial assistance for agricultural infrastructure.",
            "eligibility": "Large farmers.",
            "benefits": "Support for storage and processing units."
        },

        {
            "name": "Farm Mechanization Scheme",
            "description": "Subsidy on advanced agricultural machinery.",
            "eligibility": "Large farmers.",
            "benefits": "Modern farming equipment."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Water-saving irrigation systems.",
            "eligibility": "Large farmers.",
            "benefits": "Subsidy for irrigation."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Large farmers.",
            "benefits": "Protection against crop losses."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural finance.",
            "eligibility": "Large farmers.",
            "benefits": "Higher loan limits."
        }

    ]

}
,
"Madhya Pradesh": {

    "Small Farmer": [

        {
            "name": "Mukhyamantri Kisan Kalyan Yojana",
            "description": "Financial assistance provided by the Madhya Pradesh Government.",
            "eligibility": "Small farmers of Madhya Pradesh.",
            "benefits": "₹4,000 per year in addition to PM-KISAN benefits."
        },

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Income support scheme for eligible farmers.",
            "eligibility": "Small farmers with cultivable land.",
            "benefits": "₹6,000 per year."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance against natural calamities.",
            "eligibility": "Farmers growing notified crops.",
            "benefits": "Compensation for crop loss."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Short-term agricultural credit.",
            "eligibility": "Small farmers.",
            "benefits": "Low-interest crop loans."
        },

        {
            "name": "Soil Health Card",
            "description": "Free soil testing and fertilizer recommendations.",
            "eligibility": "All farmers.",
            "benefits": "Improves soil fertility and productivity."
        }

    ],

    "Marginal Farmer": [

        {
            "name": "Mukhyamantri Kisan Kalyan Yojana",
            "description": "Financial support for marginal farmers.",
            "eligibility": "Marginal farmers.",
            "benefits": "Additional yearly financial assistance."
        },

        {
            "name": "PM Kisan Samman Nidhi",
            "description": "Income support.",
            "eligibility": "Marginal farmers.",
            "benefits": "₹6,000 annually."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Marginal farmers.",
            "benefits": "Protection from crop failure."
        },

        {
            "name": "Seed Distribution Scheme",
            "description": "Distribution of certified seeds.",
            "eligibility": "Marginal farmers.",
            "benefits": "Improved crop productivity."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural finance.",
            "eligibility": "Marginal farmers.",
            "benefits": "Easy crop loans."
        }

    ],

    "Medium Farmer": [

        {
            "name": "Agricultural Mechanization Scheme",
            "description": "Subsidy for modern farm machinery.",
            "eligibility": "Medium farmers.",
            "benefits": "Reduced machinery costs."
        },

        {
            "name": "Mukhyamantri Kisan Kalyan Yojana",
            "description": "Financial support for cultivation.",
            "eligibility": "Medium farmers.",
            "benefits": "Additional income assistance."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance coverage.",
            "eligibility": "Medium farmers.",
            "benefits": "Protection against crop loss."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Support for drip and sprinkler irrigation.",
            "eligibility": "Medium farmers.",
            "benefits": "Water-saving subsidy."
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural credit.",
            "eligibility": "Medium farmers.",
            "benefits": "Low-interest farm loans."
        }

    ],

    "Large Farmer": [

        {
            "name": "Agricultural Infrastructure Fund",
            "description": "Financial support for agricultural infrastructure.",
            "eligibility": "Large farmers.",
            "benefits": "Loans for warehouses, cold storage and processing units."
        },

        {
            "name": "Farm Mechanization Scheme",
            "description": "Support for advanced agricultural machinery.",
            "eligibility": "Large farmers.",
            "benefits": "Subsidy on tractors and farm equipment."
        },

        {
            "name": "Mukhyamantri Kisan Kalyan Yojana",
            "description": "State financial assistance.",
            "eligibility": "Eligible farmers.",
            "benefits": "Additional yearly financial support."
        },

        {
            "name": "PM Fasal Bima Yojana",
            "description": "Crop insurance.",
            "eligibility": "Large farmers.",
            "benefits": "Compensation against crop damage."
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Drip and sprinkler irrigation support.",
            "eligibility": "Large farmers.",
            "benefits": "Subsidy for efficient irrigation."
        }

    ]

},
# ==========================================================
# ANDHRA PRADESH
# ==========================================================

"Andhra Pradesh": {

    "Small Farmer": [

        {
            "name": "YSR Rythu Bharosa",
            "description": "Financial assistance for eligible farmers.",
            "eligibility": "Small landholding farmers.",
            "benefits": "Annual financial support.",
            "website": "https://ysrrythubharosa.ap.gov.in",
            "application": "Village Secretariat / Online Portal"
        },

        {
            "name": "PM-KISAN",
            "description": "Central income support scheme.",
            "eligibility": "Eligible farmer families.",
            "benefits": "₹6,000 per year.",
            "website": "https://pmkisan.gov.in",
            "application": "CSC / Online"
        },

        {
            "name": "YSR Free Crop Insurance",
            "description": "State crop insurance.",
            "eligibility": "Registered farmers.",
            "benefits": "Compensation for crop loss.",
            "website": "State Agriculture Department",
            "application": "Agriculture Office"
        },

        {
            "name": "Kisan Credit Card",
            "description": "Low-interest agricultural loans.",
            "eligibility": "All farmers.",
            "benefits": "Easy institutional credit.",
            "website": "https://pmkisan.gov.in",
            "application": "Bank"
        },

        {
            "name": "Soil Health Card",
            "description": "Soil nutrient testing.",
            "eligibility": "All farmers.",
            "benefits": "Better fertilizer recommendations.",
            "website": "https://soilhealth.dac.gov.in",
            "application": "Agriculture Department"
        }

    ],

    "Marginal Farmer": [],
    "Medium Farmer": [],
    "Large Farmer": []

},

# ==========================================================
# TELANGANA
# ==========================================================

"Telangana": {

    "Small Farmer": [

        {
            "name": "Rythu Bandhu",
            "description": "Investment support for cultivation.",
            "eligibility": "Eligible land-owning farmers.",
            "benefits": "Seasonal financial assistance.",
            "website": "https://rythubandhu.telangana.gov.in",
            "application": "Agriculture Department"
        },

        {
            "name": "Rythu Bima",
            "description": "Farmer life insurance.",
            "eligibility": "Registered farmers.",
            "benefits": "Insurance coverage.",
            "website": "State Agriculture Department",
            "application": "Agriculture Office"
        },

        {
            "name": "PM-KISAN",
            "description": "Income support scheme.",
            "eligibility": "Eligible farmers.",
            "benefits": "₹6,000 annually.",
            "website": "https://pmkisan.gov.in",
            "application": "CSC / Online"
        },

        {
            "name": "PMFBY",
            "description": "Crop insurance scheme.",
            "eligibility": "All farmers.",
            "benefits": "Compensation for crop damage.",
            "website": "https://pmfby.gov.in",
            "application": "Bank / CSC"
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural loans.",
            "eligibility": "Farmers.",
            "benefits": "Low-interest credit.",
            "website": "https://pmkisan.gov.in",
            "application": "Bank"
        }

    ],

    "Marginal Farmer": [],
    "Medium Farmer": [],
    "Large Farmer": []

},

# ==========================================================
# HARYANA
# ==========================================================

"Haryana": {

    "Small Farmer": [

        {
            "name": "Mera Pani Meri Virasat",
            "description": "Promotes crop diversification.",
            "eligibility": "Eligible farmers.",
            "benefits": "Financial incentive.",
            "website": "State Agriculture Department",
            "application": "Agriculture Office"
        },

        {
            "name": "PM-KISAN",
            "description": "Direct income support.",
            "eligibility": "Eligible farmers.",
            "benefits": "₹6,000 annually.",
            "website": "https://pmkisan.gov.in",
            "application": "CSC"
        },

        {
            "name": "PMFBY",
            "description": "Crop insurance.",
            "eligibility": "Registered farmers.",
            "benefits": "Risk protection.",
            "website": "https://pmfby.gov.in",
            "application": "Bank"
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural loans.",
            "eligibility": "All farmers.",
            "benefits": "Affordable credit.",
            "website": "https://pmkisan.gov.in",
            "application": "Bank"
        },

        {
            "name": "Soil Health Card",
            "description": "Soil testing program.",
            "eligibility": "Farmers.",
            "benefits": "Balanced fertilizer usage.",
            "website": "https://soilhealth.dac.gov.in",
            "application": "Agriculture Department"
        }

    ],

    "Marginal Farmer": [],
    "Medium Farmer": [],
    "Large Farmer": []

},
"Andhra Pradesh": {

    "Small Farmer": [

        {
            "name": "YSR Rythu Bharosa",
            "description": "Annual financial assistance to eligible farmers.",
            "eligibility": "Small farmers",
            "benefits": "₹13,500 per year",
            "website": "https://ysrrythubharosa.ap.gov.in",
            "application": "Apply through Village Secretariat"
        },

        {
            "name": "PM-KISAN",
            "description": "Income support from Central Government.",
            "eligibility": "Eligible landholding farmers",
            "benefits": "₹6,000 annually",
            "website": "https://pmkisan.gov.in",
            "application": "CSC or PM-KISAN Portal"
        },

        {
            "name": "PMFBY",
            "description": "Crop insurance scheme.",
            "eligibility": "All farmers",
            "benefits": "Compensation for crop loss",
            "website": "https://pmfby.gov.in",
            "application": "Bank / Agriculture Office"
        },

        {
            "name": "Soil Health Card",
            "description": "Free soil testing.",
            "eligibility": "All farmers",
            "benefits": "Better fertilizer management",
            "website": "https://soilhealth.dac.gov.in",
            "application": "Agriculture Office"
        },

        {
            "name": "Kisan Credit Card",
            "description": "Low-interest agricultural loan.",
            "eligibility": "Eligible farmers",
            "benefits": "Easy institutional credit",
            "website": "https://www.pmkisan.gov.in",
            "application": "Bank"
        }

    ],

    "Marginal Farmer": [

        {
            "name": "YSR Rythu Bharosa",
            "description": "Financial support for marginal farmers.",
            "eligibility": "Marginal farmers",
            "benefits": "₹13,500 per year",
            "website": "https://ysrrythubharosa.ap.gov.in",
            "application": "Village Secretariat"
        },

        {
            "name": "PM-KISAN",
            "description": "Income assistance.",
            "eligibility": "Eligible farmers",
            "benefits": "₹6,000 annually",
            "website": "https://pmkisan.gov.in",
            "application": "CSC"
        },

        {
            "name": "PMFBY",
            "description": "Crop insurance.",
            "eligibility": "All farmers",
            "benefits": "Crop loss compensation",
            "website": "https://pmfby.gov.in",
            "application": "Bank"
        },

        {
            "name": "Kisan Credit Card",
            "description": "Agricultural credit.",
            "eligibility": "Farmers",
            "benefits": "Low-interest loans",
            "website": "https://www.pmkisan.gov.in",
            "application": "Bank"
        },

        {
            "name": "Soil Health Card",
            "description": "Soil nutrient report.",
            "eligibility": "Farmers",
            "benefits": "Improved productivity",
            "website": "https://soilhealth.dac.gov.in",
            "application": "Agriculture Office"
        }

    ],

    "Medium Farmer": [

        {
            "name": "YSR Rythu Bharosa",
            "description": "Income support scheme.",
            "eligibility": "Medium farmers",
            "benefits": "Financial assistance",
            "website": "https://ysrrythubharosa.ap.gov.in",
            "application": "Village Secretariat"
        },

        {
            "name": "PMFBY",
            "description": "Crop insurance.",
            "eligibility": "All farmers",
            "benefits": "Insurance coverage",
            "website": "https://pmfby.gov.in",
            "application": "Agriculture Office"
        },

        {
            "name": "Agricultural Mechanization Scheme",
            "description": "Subsidy on tractors and implements.",
            "eligibility": "Farmers",
            "benefits": "40–50% subsidy",
            "website": "https://apagrisnet.gov.in",
            "application": "Agriculture Department"
        },

        {
            "name": "Kisan Credit Card",
            "description": "Crop loans.",
            "eligibility": "Farmers",
            "benefits": "Low-interest credit",
            "website": "https://www.pmkisan.gov.in",
            "application": "Bank"
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Support for drip and sprinkler irrigation.",
            "eligibility": "Eligible farmers",
            "benefits": "Subsidy",
            "website": "https://apagrisnet.gov.in",
            "application": "Horticulture Department"
        }

    ],

    "Large Farmer": [

        {
            "name": "Agricultural Mechanization Scheme",
            "description": "Subsidy for advanced farm machinery.",
            "eligibility": "Large farmers",
            "benefits": "Machinery subsidy",
            "website": "https://apagrisnet.gov.in",
            "application": "Agriculture Department"
        },

        {
            "name": "PMFBY",
            "description": "Crop insurance.",
            "eligibility": "All farmers",
            "benefits": "Risk protection",
            "website": "https://pmfby.gov.in",
            "application": "Bank"
        },

        {
            "name": "Micro Irrigation Scheme",
            "description": "Subsidy for irrigation systems.",
            "eligibility": "Farmers",
            "benefits": "Efficient water management",
            "website": "https://apagrisnet.gov.in",
            "application": "Horticulture Department"
        },

        {
            "name": "Kisan Credit Card",
            "description": "Working capital support.",
            "eligibility": "Farmers",
            "benefits": "Easy crop loans",
            "website": "https://www.pmkisan.gov.in",
            "application": "Bank"
        },

        {
            "name": "Soil Health Card",
            "description": "Scientific soil analysis.",
            "eligibility": "All farmers",
            "benefits": "Balanced fertilizer use",
            "website": "https://soilhealth.dac.gov.in",
            "application": "Agriculture Office"
        }

    ]

},
# ==========================================
# Telangana
# ==========================================

"Telangana": {
    "Small Farmer": [
        {
            "name": "Rythu Bandhu Scheme",
            "description": "Investment support for crop cultivation.",
            "eligibility": "Small farmers with agricultural land.",
            "benefits": "₹10,000 per acre annually."
        },
        {
            "name": "PM-KISAN",
            "description": "Direct income support.",
            "eligibility": "Eligible farmer families.",
            "benefits": "₹6,000 per year."
        },
        {
            "name": "Rythu Bima",
            "description": "Life insurance for farmers.",
            "eligibility": "Farmers aged 18-59.",
            "benefits": "₹5 lakh insurance."
        },
        {
            "name": "PMFBY",
            "description": "Crop insurance scheme.",
            "eligibility": "Insured farmers.",
            "benefits": "Compensation for crop loss."
        },
        {
            "name": "Kisan Credit Card",
            "description": "Low-interest agricultural loans.",
            "eligibility": "All eligible farmers.",
            "benefits": "Easy farm credit."
        }
    ],

    "Marginal Farmer": "Same as Small Farmer",
    "Medium Farmer": "Same as Small Farmer",
    "Large Farmer": "Same as Small Farmer"
},

# ==========================================
# Andhra Pradesh
# ==========================================

"Andhra Pradesh": {
    "Small Farmer": [
        {
            "name": "YSR Rythu Bharosa",
            "description": "Financial assistance to farmers.",
            "eligibility": "Eligible farmers in Andhra Pradesh.",
            "benefits": "Annual income support."
        },
        {
            "name": "PM-KISAN",
            "description": "Income support scheme.",
            "eligibility": "Eligible farmers.",
            "benefits": "₹6,000 annually."
        },
        {
            "name": "PMFBY",
            "description": "Crop insurance scheme.",
            "eligibility": "Registered farmers.",
            "benefits": "Crop loss compensation."
        },
        {
            "name": "Kisan Credit Card",
            "description": "Agricultural loan facility.",
            "eligibility": "Farmers.",
            "benefits": "Easy crop loans."
        },
        {
            "name": "Soil Health Card",
            "description": "Soil testing service.",
            "eligibility": "All farmers.",
            "benefits": "Improved fertilizer usage."
        }
    ],

    "Marginal Farmer": "Same as Small Farmer",
    "Medium Farmer": "Same as Small Farmer",
    "Large Farmer": "Same as Small Farmer"
}
}


# ==========================================
# Fetch Schemes
# ==========================================

def get_schemes(state, category):

    if state not in SCHEMES:
        return []

    schemes = SCHEMES[state].get(category)

    if not schemes:
        schemes = SCHEMES[state]["Small Farmer"]

    return schemes


# ==========================================
# Gemini AI Explanation
# ==========================================

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

SCHEMES = {
    ...
}

def get_schemes(state, category):
    ...

# Replace ONLY this function ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

def generate_scheme_advice(state, category, schemes):
    ...
    # New code here

# End of file