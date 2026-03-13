        ---
        name: flask-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/flask-expert/SKILL.md
        description: Build Flask APIs with blueprints, application factory, and proper error handling.
        ---

        You build well-structured Flask applications.

## Application Factory Pattern
```python
def create_app(config=None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config or ProductionConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    @app.errorhandler(ValidationError)
    def handle_validation(e):
        return jsonify(error=str(e)), 400

    return app
```

## Rules
- Always use application factory — never instantiate `Flask` at module level.
- Blueprints for each domain area (auth, users, admin).
- Error handlers for all custom exception types at app level.
- Use `current_app.config` inside views, not global config objects.
