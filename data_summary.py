df.agg(F.sum(F.col('diff1'))).first()[0]
