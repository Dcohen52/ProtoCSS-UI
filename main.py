from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    btn_classes = [
        "btn",
        "btn-primary",
        "btn-secondary",
        "btn-success",
        "btn-danger",
        "btn-warning",
        "btn-info",
        "btn-light",
        "btn-dark",
        "btn-custom",
        "btn-disabled",
        "btn-icon",
        "btn-full",
        "btn-rounded",
        "btn-small",
        "btn-large",
        "btn-outline",
        "btn-border",
        "btn-shadow",
        "btn-gradient",
        "btn-underline",
        "btn-fade",
        "btn-spin",
        "btn-border-shadow",
        "btn-outline-alt",
        "btn-hover-shadow",
        "btn-gradient-alt",
        "btn-hover-underline",
        "btn-grow"
    ]
    table_classes = [
        "table",
        "table-sm",
        "table-bordered",
        "table-hover",
        "table-primary",
        "table-secondary",
        "table-success",
        "table-info",
        "table-warning",
        "table-danger",
        "table-light",
        "table-dark",
        "table-active",
        "thead-dark",
        "thead-light",
        "table-responsive-sm",
        "table-responsive-md",
        "table-responsive-lg",
        "table-responsive-xl",
        "table-responsive"
    ]
    class_names = [
        "center",
        "left",
        "right",
        "top",
        "bottom",
        "jc-sb",
        "jc-sa",
        "vertical",
        "horizontal",
        "d-flex",
        "d-inline-flex",
        "d-grid",
        "d-inline-grid",
        "d-block",
        "d-inline",
        "jc-start",
        "jc-end",
        "jc-center",
        "jc-space-between",
        "jc-space-around",
        "jc-space-evenly",
        "ai-align-start",
        "ai-align-end",
        "ai-align-center",
        "ai-align-stretch",
        "ai-align-baseline",
        "ac-start",
        "ac-end",
        "ac-center",
        "ac-space-between",
        "ac-space-around",
        "space-evenly",
        "center",
        "center-horizontal",
        "center-vertical",
        "center-horizontal-top",
        "center-horizontal-bottom",
        "center-vertical-left",
        "center-vertical-right"
    ]
    colors = [
        "text-primary",
        "text-secondary",
        "text-success",
        "text-danger",
        "text-warning",
        "text-info",
        "text-light",
        "text-dark",
        "text-custom"
    ]
    bg_colors = [
        "bg-primary",
        "bg-secondary",
        "bg-success",
        "bg-danger",
        "bg-warning",
        "bg-info",
        "bg-light",
        "bg-dark",
        "bg-transparent"
    ]

    return render_template('index.html', btn_classes=btn_classes, table_classes=table_classes, class_names=class_names,
                           colors=colors, bg_colors=bg_colors)


@app.route('/button-click', methods=['POST'])
def handle_button_click():
    button_name = request.form.get('button')
    print(f"Button clicked: {button_name}")
    return jsonify(message="Button click handled successfully")


if __name__ == '__main__':
    app.run()
