# AI-Production-System-Forward-Backward-Chaining
This project is a simple AI **Production System** built using Python and Streamlit. It supports both **Forward Chaining** and **Backward Chaining** inference algorithms. The system reads rules and facts from uploaded text files and displays inferred knowledge with a user-friendly interface.

![image](https://github.com/user-attachments/assets/6986e358-b16e-4fe7-9997-00e28aff2dc6)

Features
-  Upload `rules.txt` and `facts.txt` via web interface
-  Run **Forward Chaining** to infer new facts
-  Run **Backward Chaining** to test if a goal can be reached
-  View facts at each reasoning cycle (step-by-step tracing)
-  Input a custom goal for both algorithms
-  Streamlit-powered clean UI for easy interaction

How to use:

    - Run the app:
        Open a terminal and run:    streamlit run streamlit_app.py
    - Use the Interface
          Once the app opens in your browser:
              - Upload your rules.txt and facts.txt files.
              - Choose the inference algorithm from the dropdown:
                      - Forward Chaining: Automatically infers all possible facts from the initial ones.
                      - Backward Chaining: Starts from a goal and tries to prove it.
              - Enter a goal to check
              - View the output:
                    - Inferred facts
                    - Whether the goal was reached
                    - Step-by-step reasoning 
