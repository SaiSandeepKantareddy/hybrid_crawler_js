# Basic end-to-end test placeholder
import asyncio
import os
import pandas as pd
from pipeline.hybrid_runner import main as run_pipeline

def test_hybrid_crawler():
    print(" Running end-to-end hybrid crawler test...")

    # Use test config
    config_path = "pipeline/config.yaml"

    # Remove old output if it exists
    output_file = "data/hybrid_output.csv"
    if os.path.exists(output_file):
        os.remove(output_file)

    # Run pipeline
    asyncio.run(run_pipeline(config_path))

    # Check output
    assert os.path.exists(output_file), " hybrid_output.csv not created."
    df = pd.read_csv(output_file)
    assert not df.empty, " Output file is empty."
    assert "used_js" in df.columns, " used_js column missing."
    assert "score" in df.columns, " score column missing."

    print(" End-to-end test passed!")
    print(df[["url", "used_js", "score", "error"]].head())


if __name__ == "__main__":
    test_hybrid_crawler()
