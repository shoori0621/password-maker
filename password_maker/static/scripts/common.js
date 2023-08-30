// パスワードをコピー
function passwordCopy(id) {
  axios
    .get(
      `http://127.0.0.1:8000/api/password_maker/accounts/${id}/decrept_password`
    )
    .then((result) => {
      copyToClipboard(result.data);
    })
    .catch((err) => {
      console.log(err);
      toastr.error("パスワードがコピーできませんでした");
    });
}

// クリップボードへコピー（コピーの処理）
function copyToClipboard(tagValue) {
  if (navigator.clipboard) {
    return navigator.clipboard.writeText(tagValue).then(function () {
      toastr.success("パスワードをコピーしました");
    });
  }
}
