# Surgical Checklist Tracking Program

This program is designed to automate the tracking of checklists used during surgical operations. It helps surgeons and medical staff ensure that all necessary steps and procedures are followed, improving patient safety and the quality of care.

## Features

- **Create New Checklist**: Allows you to create a new checklist for a surgical operation, filling out all necessary steps.
- **Track Step Completion**: The program tracks the completion status of each step in the surgery (completed/not completed).
- **Save Data**: All data regarding checklists and operations are saved in a database for future analysis.
- **Search Checklists**: Enables searching by various criteria (e.g., patient name, operation date, type of surgery).
- **Reporting**: Generate reports on checklist completion, enabling analysis of operational efficiency and adherence to medical standards.

## Usage

1. Launch the program.
2. In the main window, select the type of surgery from the available options.
3. For each surgery, mark the completion of all necessary steps.
4. Once the surgery is complete, save the checklist.
5. Use the search function to review completed operations and their checklists.

## Data Structure

The checklist consists of the following data:

- **Patient**: Patient's full name
- **Surgery Date**: Date and time of the surgery
- **Type of Surgery**: A brief description of the surgical procedure
- **Surgery Steps**: A list of all steps that should be completed during the surgery. Each step can be marked as completed or not completed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
