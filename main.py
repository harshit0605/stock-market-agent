from workflows.main_workflow import create_workflow

def main():
    workflow = create_workflow()
    result = workflow.invoke({"query": "Analyze AAPL stock"})
    print(result["final_recommendation"])

if __name__ == "__main__":
    main()