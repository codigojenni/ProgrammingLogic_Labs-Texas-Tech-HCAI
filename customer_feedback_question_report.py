def extract_questions():
    input_file = "customer_feedback.txt"
    output_file = "questions_report_John_Doe.txt"

    try:
        file = open(input_file, "r")
        lines = file.readlines()
        file.close()

        question_entries = []
        total_feedbacks = 0
        total_questions = 0

        for line in lines:
            if "||" not in line:
                continue  
            total_feedbacks += 1
            parts = line.strip().split("||")
            name = parts[0].strip()
            feedback = parts[1].strip()

            sentences = feedback.split(".")

            for sentence in sentences:
                if "?" in sentence:
                    question = sentence.strip() + "?"
                    question_entries.append((name, question))
                    total_questions += 1

        report = open(output_file, "w")
        report.write("**************************************\n")
        report.write("** Report of Questions by Customers **\n")
        report.write("**************************************\n")

        question_number = 1
        for entry in question_entries:
            name, question = entry
            report.write(f"{question_number}) {name} asked: {question}\n")
            question_number += 1

        report.write("------------------------------------------------------\n")
        report.write("No. of Feedbacks Processed: " + str(total_feedbacks) + "\n")
        report.write("No. of Extracted Questions: " + str(total_questions) + "\n")
        report.write("*************************************\n")
        report.close()

        print("Report created successfully!")

    except:
        print("Something went wrong. Please check the input file.")

extract_questions()
