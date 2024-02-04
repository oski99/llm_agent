## llm_agent

my master thesis - tabular data analysis using llms

solution? - llm agent having access to python repl

uses `langchain` and `llamacpp`

![agent](https://github.com/oski99/llm_agent/assets/102487659/0f52c3d9-042e-45cb-8219-5409962669e0)

### QUESTIONS:

    1. What are the basic statistical summaries for each column in the dataset?

    2. Are there any outliers in the data? If so, in which columns?

    3. Which columns have missing data and what is the percentage of missing data in those columns?

    4. Choose two numerical columns. Can you create a scatter plot to show the relationship between them?

    5. Create a histogram for the first column.

    6. Which columns have the highest correlation?

    7. Use Random Forest to predict the values for the nth column based on the other attributes.

    8. Standardize the first column.

    9. Are there any duplicate rows in the dataset?

    10. Extract the top 5 highest values from the first column.

### RESPONSE CLASSIFICATION

    final answer: correct || misstep || wrong

    RA  - redundant actions

    H   - hallucination

*response sneek peeks correct tools/solution

## Easy Dataset         - Numerical Attributes, No Missing Values

| QID | gpt-4-turbo-preview | gpt-3.5-turbo-instruct | mistral-7b-instruct-v0.2 | 
|:---:|:-------------------:|:----------------------:|:------------------------:|
|1    | correct             | misstep                | correct                  |
|2    | correct             | misstep + H            | misstep + H              | 
|3    | correct             | correct                | correct + RA             |
|4    | correct             | correct                | correct + RA             |
|5    | correct             | correct + RA           | correct                  |
|6    | correct             | correct + RA           | wrong                    |
|7    | correct             | correct                | correct + RA             |
|8    | correct             | correct                | misstep                  |
|9    | correct             | correct                | wrong                    |
|10   | correct             | correct                | misstep                  |

## Hard Dataset         - Mixed Data Types, With Missing Values

| QID | gpt-4-turbo-preview | gpt-3.5-turbo-instruct | mistral-7b-instruct-v0.2 |
|:---:|:-------------------:|:----------------------:|:------------------------:|
|1    | misstep             | misstep                | misstep                  |
|2    | correct             | misstep + H            | wrong                    |
|3    | correct             | correct                | misstep                  |
|4    | correct             | wrong                  | wrong                    |
|5    | correct             | correct                | correct                  |
|6    | correct             | misstep                | wrong                    |
|7    | misstep             | misstep                | misstep + H              |
|8    | correct + RA        | correct                | correct + RA             |
|9    | correct             | correct + RA           | correct                  |
|10   | correct             | correct + RA           | correct                  |


## Inference speed (token/s)

| model                           | speed |
|:-------------------------------:|:-----:|
| gpt-4-turbo-preview             | 16.63 |
| gpt-3.5-turbo-instruct          | 54.69 |
| mistral-7b-instruct-v0.2.Q5_K_M | 7.97  |
| llama-2-7b-chat.Q5_K_M          | 8.76  |
| llama-2-13b-chat.Q4_K_M         | 3.60  |