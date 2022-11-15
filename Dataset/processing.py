import xgboost as xgb

def create_dtrain(df, cols, tar, idx):
    return xgb.DMatrix(data=df.iloc[idx][cols],label=df.iloc[idx][tar])