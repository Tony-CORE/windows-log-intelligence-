import pandas as pd

def analyze_windows_event_failures(file_path):
    """
    Analyze Windows Event Logs to identify critical operational issues.
    Focused on errors commonly seen during patching, authentication failures,
    and service crashes in enterprise environments.
    """

    pd.read_csv("../data/eventlog_sample.csv")

    # Filter only Error and Critical logs (operational relevance)
    df = df[df["Level"].isin(["Error", "Critical"])]

    # Event IDs commonly observed in enterprise Windows environments
    # 4625 - Failed Logon
    # 7036 - Service state changes
    # 1000 - Application crash
    critical_event_ids = [4625, 7036, 1000]
    df = df[df["EventID"].isin(critical_event_ids)]

    summary = (
        df.groupby(["EventID", "Source"])
        .size()
        .reset_index(name="OccurrenceCount")
        .sort_values(by="OccurrenceCount", ascending=False)
    )

    return summary


if __name__ == "__main__":
    result = analyze_windows_event_failures("../data/eventlog.csv")
    print(result)
