function formCheck() {
    // 모든 답변 DOM 객체(input type radio)를 가져옴
    answerList = document.getElementsByClassName("answer");
    // console.log(answerList);

    // 답변 선택 여부를 저장할 변수 선언 및 false로 초기화.
    let isChecked = false;

    // 반복문을 통해서 모든 답변 DOM 객체를 하나씩 꺼내오며 검사. 
    for (let i = 0; i < answerList.length; i++) {
        // console.log(answerList[i].checked);
        if (answerList[i].checked) {
            // input type radio의 checked 속성 값이 true인 경우,
            // 위에서 선언한 isChecked 변수의 값을 true로 바꾸고 반복문을 중단.
            isChecked = true;
            break;
        }
    }

    if (isChecked) {
        return true; // 선택한 답변이 있는 경우, 양식을 제출하도록 true 반환.
    } else {
        // 선택한 답변이 없는 경우, 양식이 제출되지 않도록 false 반환.
        alert("답변을 선택해주세요.");
        return false;  
    }
}   