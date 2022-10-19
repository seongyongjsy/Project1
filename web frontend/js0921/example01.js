window.onload = function() {
    // keyup: 키보드의 키가 눌렸다가 떼어지는 순간을 인식해서 실행하는 이벤트 종류.
    // 키가 눌려지자마자 input 태그에 바로 데이터가 입력되는 게 아니기 떄문에,
    // 확실하게 데이터가 입력되고 키보드가 떼어지면 실행하는 이벤트로서,
    // 키보드 관련 이벤트 중 가장 많이 사용하는 이벤트.
    // cf)keydown, keypress, keyup
    document.getElementById("id-input").addEventListener("keyup", function(e) {
        // console.log(e); // Keyboard 이벤트 객체. 어떤 키를 입력했는지 확인 가능.
        console.log(this);  // 이벤트 함수를 실행시킨 주체.
        
        // let idTxt = document.getElementById("id-input").value;
        let idTxt = this.value;
        // console.log(idTxt);

        if(idTxt.length < 4 || idTxt.length > 8) {
            // ID 입력란에 입력한 글자 수가 4~8 글자 사이가 아닌 경우,
            // 입력란의 배경 색깔을 강조 표시함.
            // document.getElementById("id-input").style = "background-color: orange;"
            document.getElementById("id-input").className = "err";
            document.getElementById("id-msg").innerText = "ID 글자 수를 확인해주세요.";
        } else {
            // ID 입력란에 입력한 글자 수가 4~8 글자 사이인 경우,
            // 입력란의 배경 색깔을 원래대로 되돌림.
            // document.getElementById("id-input").style = "background-color: white;";
            document.getElementById("id-input").className = "";
            document.getElementById("id-msg").innerText = "사용할 수 있는 ID입니다.";
        }
        if (idTxt.length > 8) {
            // ID 입력란에 입력한 글자 수가 8글자를 넘어가는 경우,
            // 입력한 텍스트 중 9글자 이후의 글자를 잘라서 없애버림.
            document.getElementById("id-input").value = idTxt.substr(0,8);
            // document.getElementById("id-input").style = "background-color: white;"
            document.getElementById("id-input").className = "";
        }
    });

    // focus: 입력란이 클릭되었을 때 실행하는 이벤트.
    document.getElementById("id-input").addEventListener("focus", function() {
        this.style = "border: 3px dashed green;";
    });
    // blur: 입력란을 클릭 해제했을 때 실행하는 이벤트.
    document.getElementById("id-input").addEventListener("blur", function() {
        this.style = "";
    });

    // mouseenter: 대상 요소에 마우스 커서가 올려지면 실행하는 이벤트
    document.getElementById("submit-btn").addEventListener("mouseenter", function() {
        this.style = "border: 5px ridge gray;";
    });
    // mouseleave: 대상 요소에 마우스 커서가 벗어나면 실행하는 이벤트
    document.getElementById("submit-btn").addEventListener("mouseleave", function() {
        this.style = "";
    });

    
    let genderRadios = document.getElementsByClassName("gender-radio"); // 모든 라디오 버튼을 선택
    for (let i = 0; i < genderRadios.length; i++) { // 반복하면서 모든 라디오 버튼에 이벤트를 적용.
        // change: 입력란의 값이 변경되면 실행하는 이벤트. 
        // input type = text, password, number, date, checkbox, radio, file
        // select, textarea 등의 태그에서 사용
        genderRadios[i].addEventListener("change", function() {
        // 이벤트가 실행되면 다시 한 번 모든 라디오 버튼에 대해서 반복하면서 검사를 진행.
        for (let i = 0; i < genderRadios.length; i++) {
            if (genderRadios[i].checked) {
                // 선택된 라디오 버튼의 경우, 강조 표시를 추가함.
            genderRadios[i].parentNode.style = "border: 3px dotted orange;";
            } else {
                // 선택되지 않은 라디오 버튼의 경우, 강조 표시를 제거함.
            genderRadios[i].parentNode.style = "border: 3px dotted #00000000";
            }
        }     
    });
    }

    // on이벤트 속성을 이용해서 HTML 태그에서 직접 적용시킬 이벤트 함수이기 때문에,
    // 굳이 페이지 로딩이 끝난 후 함수를 작성하거나 적용시킬 필요가 없음.
    function formCheck() {
        // ID 글자 수 검사.
        let idTxt = document.getElementById("id-input").value;
        if (idTxt.length < 4 || idTxt.length > 8 ) {
            alert("ID 글자 수를 확인해주세요.")
            return false;   // 검사를 통과하지 못한 경우, 양식이 제출되지 않도록 false를 반환함.
        }
        // 비밀번호 글자 수 검사.
        let pwTxt = document.getElementById("pw-input").value;
        if (pwTxt.length < 4 || pwTxt.length > 8) {
            alert("비밀번호 글자 수를 확인해주세요.");
            return false;
        }
        // 비밀번호 일치 여부 검사
        let pwChkTxt = document.getElementById("pw-input-check").value;
        if (pwChkTxt != pwTxt) {
            alert("입력하신 비밀번호를 확인해주세요.");
            return false;
        }

        return true;    // 모든 검사를 통과한 경우, 양식 제출이 되도록 true를 반환함
    }
}