# Functions for metrics and logging placeholder
import pandas as pd

def compute_summary_metrics(df: pd.DataFrame) -> dict:
    total = len(df)
    if total == 0:
        return {}

    num_js = df['used_js'].sum()
    avg_score = df['score'].mean()
    num_errors = df['error'].notnull().sum()
    avg_content_length = df['content'].apply(len).mean()

    return {
        "total_pages": total,
        "js_rendered_pages": int(num_js),
        "js_rendered_%": round((num_js / total) * 100, 2),
        "avg_score": round(avg_score, 3),
        "error_rate_%": round((num_errors / total) * 100, 2),
        "avg_content_length": int(avg_content_length)
    }


def print_summary(metrics: dict):
    print("\n Summary Metrics:")
    for k, v in metrics.items():
        print(f"{k:>20}: {v}")


# Example usage
if __name__ == "__main__":
    df = pd.read_csv("data/hybrid_output.csv")
    metrics = compute_summary_metrics(df)
    print_summary(metrics)
