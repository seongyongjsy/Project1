$(function() {
    $("input:text").keyup(idCheck);  // ID 입력란에 키보드의 키가 입력된 상황을 인식해서 이벤트 실행.
    $("input:password").keyup(pwCheck);  // 비밀번호 입력란에 키보드의 키가 입력된 상황을 인식해서 이벤트 실행.
    $("input:button").click(formCheck);  // 로그인 버튼이 클릭되면 양식 검사 함수 실행.

    $("input:text").keyup(enterCheck); // ID 입력란에 엔터 키를 입력한 경우 처리할 이벤트.
    $("input:password").keyup(enterCheck);  // 비밀번호 입력란에 엔터 키를 입력한 경우 처리할 이벤트.

    $("input:text, input:password").css("border", "3px solid black");
    // 입력란에 대해 focus, blur 상황이 발생하면 강조 표시/해제.
    $("input:text").focus(function() { $(this).css("border", "3px dashed orange"); });
    $("input:text").blur(function() { $(this).css("border", "3px solid black"); });
    $("input:password").focus(function() { $(this).css("border", "3px dashed orange"); });
    $("input:password").blur(function() { $(this).css("border", "3px solid black"); });

    $("input:button").css({"color": "black", "background-color": "white"});
    // 로그인 버튼에 마우스 커서가 올라갈 때/벗어날 때 CSS를 변경하는 이벤트.
    // $("input:button").mouseenter(function() { $(this).css({"color": "white", "background-color": "black"}); });
    // $("input:button").mouseleave(function() { $(this).css({"color": "black", "background-color": "white"}); });
    $("input:button").hover(
        function() { $(this).css({"color": "white", "background-color": "black"}); },
        function() { $(this).css({"color": "black", "background-color": "white"}); }
    );
});

// ID 입력란 검사 함수.
function idCheck() {
    // ID 글자 수를 검사해서 적당한 알림 메시지를 출력.
    // console.log(this.value);  // 자바스크립트 DOM 객체에서 value 속성값 추출.
    // console.log($(this).val());  // 자바스크립트 DOM 객체를 제이쿼리 객체로 포장하고 val() 메소드로 value 속성값 추출.
    let idLength = $("input:text").val().length;
    if (idLength < 4 || idLength > 8) {
        $("div#id-msg").text("ID를 확인해주세요.");
        $("div#id-msg").css("color", "red");
        return false;
    } else {
        $("div#id-msg").text("사용할 수 있는 ID입니다.");
        $("div#id-msg").css("color", "green");
        return true;
    }
}

// 비밀번호 입력란 검사 함수.
function pwCheck() {
    // 비밀번호 글자 수를 검사해서 적당한 알림 메시지를 출력.
    let pwLength = $("input:password").val().length;
    if (pwLength < 8 || pwLength > 12) {
        $("div#pw-msg").text("비밀번호를 확인해주세요.");
        $("div#pw-msg").css("color", "red");
        return false;
    } else {
        $("div#pw-msg").text("사용할 수 있는 비밀번호입니다.");
        $("div#pw-msg").css("color", "green");
        return true;
    }
}

// 양식 제출 전 검사 함수.
function formCheck() {
    // ID 글자 수 검사.
    if (idCheck() === false) {
        alert("ID를 확인해주세요.");
        return;
    }

    // 비밀번호 글자 수 검사.
    if (pwCheck() === false) {
        alert("비밀번호를 확인해주세요.");
        return;
    }

    // 모든 검사를 통과한 경우, 양식을 제출(=form 데이터를 전송).
    $("form").submit();
}

// 입력란에 대한 엔터 키 검사 함수.
function enterCheck(e) {
    // 만약 방금 입력한 키가 엔터 키라면 양식을 제출(=form 데이터를 전송).
    // console.log(e.key);
    if (e.key == "Enter") formCheck();
}