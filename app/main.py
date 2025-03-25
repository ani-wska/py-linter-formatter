def format_linter_error(error: dict) -> dict:
    return{key: value for key, value in error.items()}



def format_single_linter_file(file_path: str, errors: list) -> dict:
    return{"errors": [errors], "file_path": file_path, "status": "failed"}



def format_linter_report(linter_report: dict) -> list:
    return[
        {
            "errors": [format_linter_error],
            "file_path": format_single_linter_file(linter_report["file_path"], linter_report["errors"]),
            "status": linter_report["status"]
        }

]

