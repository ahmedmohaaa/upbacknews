CKEDITOR.plugins.add('customImageUpload', {
    icons: 'image',
    init: function (editor) {
        editor.addCommand('openImageDialog', {
            exec: function () {
                editor.execCommand('image');
            }
        });
        editor.ui.addButton('CustomImageUpload', {
            label: 'إدراج صورة',
            command: 'openImageDialog',
            toolbar: 'insert'
        });
    }
});
