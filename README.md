# Probabilistic Market Regime & Range Forecasting Dashboard

*A real-time FastAPI + React application for multi-timeframe session classification, conditional probability modeling, and robust regression-based range forecasting.*

## Overview

This project implements a **live trading analytics system** that connects to the **Topstep ProjectX API** to stream ES futures data.  
It processes **1-minute bars**, aggregates them into **1H and 4H structures**, and applies:

- **Markov-based candle classification** for probabilistic regime tracking  
- **Conditional probability filtering** using historical snapshots  
- **Robust regression (Huber) models** to forecast expected ranges  

The results are streamed to a **React-based dashboard** in real time via **FastAPI WebSockets**, providing a probabilistic and statistical perspective on evolving market structure enabling rigorous, data-driven decision-making  

### Conditional Probability Framework
- A core component of the system is the **snapshot-based conditional probability engine**. Each session (1H or 4H) is classified based on its interaction with prior session highs and lows, forming the foundation for regime-aware analysis.  
- Users can apply **customizable filters** through the dashboard—such as prior-day high/low taken, relative range expansions etc. —to narrow probabilities to specific structural contexts.  
- These conditional probabilities are recomputed **live every minute** as new data arrives, ensuring that evolving market structure continuously updates the probability distributions. This provides traders with a dynamic, real-time statistical view of potential outcomes rather than static backtested signals.  

⚠️ For details on how the probability model is constructed, refer to **Session Classification Markov Model** in the repository  
💻 The code for the frontend can be found at https://github.com/aryapratham000/trading-dashboard-frontend

## Features & Project Structure 

- **Authentication & Config Management** – API login via key/token (`auth.py`, `config.py`)
- **Historical & Live Data** – 1-minute bar retrieval, higher-timeframe aggregation (`data.py`)
- **Session Classification** – Markov-style color coding across sessions (`candleClassification.py`)
- **Daily Levels & VWAP** – automated computation and live updating of pdHigh, pdLow, NY Open, VWAP, etc. (`dailyLevels.py`)
- **Conditional Probabilities** – Live probability filtering with session classification and customizable conditions (`markov_model.py`)
- **Range Forecasting** – robust ML models (Huber regression) for **1H & 4H range prediction** (`range_model.py`)
- **Real-Time Backend** – FastAPI WebSocket server delivering structured market snapshots & predictions (`main.py`)
- **Frontend Dashboard** – React-based interface auto-launched for visualization (`start.py`)

## Frontend Preview
Check it out at https://trading-dashboard-frontend-taupe.vercel.app/

<img width="504" height="385" alt="image" src="https://github.com/user-attachments/assets/b2372cd0-726e-4fa4-9530-19f0d8356de8" />

<img width="504" height="385" alt="image" src="https://github.com/user-attachments/assets/9391a99d-2fd4-4e15-b264-594b3994ab3c" />


## Project Structure
- `auth.py` — Authentication with ProjectX API  
- `config.py` — API credentials & base URL  
- `data.py` — Historical + live bar fetching, aggregation  
- `dailyLevels.py` — Prior-day levels, VWAP, rolling high/low  
- `candleClassification.py` — Markov-based candle classification  
- `markov_model.py` — Conditional probability filtering, event probs  
- `range_model.py` — Feature engineering & robust regression models  
- `main.py` — FastAPI backend, WebSocket streaming  
- `start.py` — Launcher for backend + frontend  
- `dashboard/` — React frontend (npm run dev)  

## Models & Data Dependencies

### Pretrained Models
- `huber_1h_*.pkl` → Robust regression model for **1H range prediction**  
- `huber_4h_*.pkl` → Robust regression model for **4H range prediction**

### Snapshot Data
- `df_1h_snapshots.parquet`  
- `df_4h_snapshots.parquet`  

Used for **conditional probability filtering** & **quantile thresholds**.


## Development Pipeline
- Extend coverage to multiple instruments beyond ES (e.g., NQ, CL, FX futures)
- Introduce an ML-based breakout probability model to estimate the likelihood of RTH highs or lows being broken, conditioned on time-since-extreme features, trend structures, and session context
- Add support for **multi-factor features** (macro events, VIX, earnings news) in range forecasting models
- Integrate **alerts & notifications** (email/Slack) for key probability thresholds
- Develop a **Macro & News Intelligence Layer** that summarizes daily news, global events, and earnings reports using LLMs, providing a complementary fundamental perspective alongside the quantitative probability models
- LLM powered "Smart Context" feature that describes recent market movement and how traders can best position themselves  



