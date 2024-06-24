
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/3544qsn656kc/Llama2Tutorial/workflows/workflow-2ce1b3"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="3dcb4aaf6f3343c98724240bb300c849"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
