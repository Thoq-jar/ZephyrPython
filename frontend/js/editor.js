document.addEventListener('DOMContentLoaded', () => {
    var editor = CodeMirror.fromTextArea(document.getElementById("editor"), {
        lineNumbers: true,
        theme: "default",
        mode: "python"
    });
});
