// パスワードをコピー
function passwordCopy(password) {
  copyToClipboard(password);
}

// クリップボードへコピー（コピーの処理）
function copyToClipboard(tagValue) {
  if (navigator.clipboard) {
    return navigator.clipboard.writeText(tagValue).then(function () {
      toastr.success("パスワードをコピーしました");
    });
  }
}
