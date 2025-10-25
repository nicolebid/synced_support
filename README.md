# Synced Support  

A dashboard application intended for Learning Support Teachers (aka Resource Teachers) or teachers who  manage caseloads and support students across all their subjects. 

## 🎯 Motivation 

Learning Support Teachers typically work with students who have diverse learning needs. Keeping track of deadlines, supporting students in completing assignments, communicating with classroom teachers, and ensuring students receive essential accommodations is only part of what these teachers do. With caseloads ranging from 10 to 40 students, each with up to 8 teachers, this becomes a complex and demanding task.

This application simplifies these tasks for teachers by providing an interactive dashboard where they can easily track upcoming deadlines, filter and view student schedules, monitor work habits and attendance, and gain insight into students progress—all in one convenient location that streamlines and optimizes their workflow.

## ▶️ Try out the App!

Check out the dashboard (pre-filled with sample data) here: [Synced Support](<link>).

- Student View: Explore student profiles with daily schedules, work and attendance habits, and add personalized notes or observations.

- Task View: Track upcoming deadlines, filter by student or teacher, add new tasks, and keep track of what task each student needs to complete. 

![Demo](<directory with gif>)

## 🤝 Support the Project!

If you are interested in contributing to the development of the Solar Savers dashboard, please read the [contributing guidelines](CONTRIBUTING.md) for full details. Below are some quick steps to run the dashboard locally. 

#### Run the App Locally

1. Clone the repository locally. In your terminal run:

    ```console
    $ git clone <link>
    ```

2. Create and activate the `conda` environment. In the root of the repository run:
    ```console
    $ conda env create --file environment.yml
    ```

    ```console
    $ conda activate <name>
    ```

3. Create a branch for local development and make your changes:

    ```console
    $ git checkout -b name-of-your-fix-or-feature
    ```

4. To run the dashboard, from the root of the directory (<name>) run: 

    ```console
    $ python -m src.app
    ```
5. Click on the displayed link to view the dashboard on a browser.

#### Contributing Guidelines

Interested in contributing to this project? Check out the [contributing guidelines](CONTRIBUTING.md). *Please note: This project is released with a Code of Conduct. By contributing to this project, you agree to abide by the terms in the [Code of Conduct](CODE_OF_CONDUCT.md).* 

## 📌 Contact Me

If you'd like to suggest a new feature or if you experience a problem while using the dashboard, please open an [issue](<link>). For problems, please include: 

- A description of the problem, indicating details that would be helpful in troubleshooting.
- Detailed steps to reproduce the problem.

## 📄 License

Synced Support is developed and maintained by Nicole Bidwell. The code is licensed under the MIT License and Creative Commons License. Please see [LICENSE.md](LICENSE.md) for details.  
