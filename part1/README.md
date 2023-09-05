# Part 01 - JWT Based Authentication System

[Youtube Video](https://www.youtube.com/watch?v=qG-tpH-KbSg)

## Table of Contents

1. [Tech Stack Used](#tech-stack-used)
2. [Project Description](#project-description)
3. [Issues Faced](#issues-faced)
4. [Approach Used](#approach-used)
5. [Installation](#installation)
6. [Contributing](#contributing)
7. [Contact Developer](#contact-developer)

## Tech Stack Used

- HTML/CSS
- JavaScript
- Flask
- Python
- JWT

## Project Description

This assignment aims to build an Authentication and an Image Upload API Functionality.

## Issues Faced

- Storing Session of user
- Including JWT Authentication System
- Building API Script to test the throttle limit

## Approach Used

1. **Setup**:

   - Create a Flask project structure.
   - Set up a virtual environment.
   - Initialize a Flask app.

2. **UI**:

   - Design a basic HTML form for image uploads.
   - Use a Flask route to process uploads.
   - Display uploaded image names.

3. **Authentication**:

   - Implement JWT-based user authentication.
   - Create registration for API keys.
   - Protect API routes with JWT validation.

4. **Rate Limiting**:

   - Enforce a 5 requests/minute rate limit.
   - Use middleware to track requests.
   - Return error responses for limit breaches.

5. **Testing**:

   - Develop a Python script for rate limit testing.
   - Validate rate limiting functionality.

6. **Deployment**:

   - Choose a hosting platform, I personally choosen Render.
   - Deploy the application.

7. **Documentation**:

   - Create a README with setup and usage instructions.

## Installation

To run this assignment locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/theanantchoubey/flaskAuthenticationSystem.git
   ```

2. Go the Part 01 of the Repository

   ```
   cd part1
   ```

3. Install all the packages listed in requirements.txt

   ```
   pip install -r requirements.txt
   ```

4. Run the Python App
   ```
   python app.py
   ```

## Contributing

If you'd like to contribute to this project or want to suggest any improvements please make sure to raise an Issue and discuss with the developer. Please contact - [anantchoubey039@gmail.com](mailto:anantchoubey039@gmail.com)

## Contact Developer

[LinkedIn](https://www.linkedin.com/in/theanantchoubey/)
[Twitter](https://twitter.com/theanantchoubey)
