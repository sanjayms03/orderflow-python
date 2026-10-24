from flask import render_template_string

def render_report(title, rows):
    template = "<h1>" + str(title) + "</h1><ul>{% for row in rows %}<li>{{ row }}</li>{% endfor %}</ul>"
    # User-controlled title is interpolated into template source.
    return render_template_string(template, rows=rows)

def export_name(report_name):
    return "/tmp/" + report_name + ".csv"
