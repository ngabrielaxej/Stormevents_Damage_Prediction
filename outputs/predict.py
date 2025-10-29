#!/usr/bin/env python3
import sys, pandas as pd, numpy as np, joblib
def main(inp,out):
    bprop=joblib.load("results/xgb_tweedie_property.joblib")
    bcrop=joblib.load("results/xgb_tweedie_crop.joblib")
    pre=joblib.load("results/preprocess.joblib")
    df=pd.read_csv(inp)
    X=pre.transform(df)
    p_prop=bprop.predict(X); p_crop=bcrop.predict(X)
    pd.DataFrame({"pred_damage_property":p_prop,"pred_damage_crops":p_crop}).to_csv(out,index=False)
if __name__=="__main__": main(sys.argv[1], sys.argv[2])
