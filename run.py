"""
This module initializes and runs the Flask application.

It creates the app instance and runs it in debug mode when executed directly.
"""

from app import create_app

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    # Run the app in debug mode when this script is executed directly
    app.run(debug=False, host="0.0.0.0", port=5000)
