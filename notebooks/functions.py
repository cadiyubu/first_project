# ============================================================
# functions.py — Shared utilities for CO₂ & Energy project
# ============================================================
# Both EDA notebooks (Diana & Irene) import from this file.
# All analysis logic is currently written inline in the notebooks.
# This file is reserved for reusable functions if any are extracted.
# ============================================================

# Shared imports used across project notebooks
import yaml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import logging
import sys
from pathlib import Path
from scipy import stats
