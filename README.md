# 컴퓨터 네트워크 과제

## 1번
https://cau-cpss.github.io/ComputerNetwork/assets/js/rress.js 에 접속 후 해당 코드를 확인:

```javascript
import { _______________, _______, _____, __________, ___________, ____________, _____________, ______________  } from './crypt.js';

window.counter = 0;

let cipher = `:)\x1FV4Y\x14\x0060B\x07:\x02D1?()\r=2;\b>\x00\x03\x115.) *\v3\x05&<9\x07=\x02*\\8&#\x1A=\x1F\x07\b9\x02\x10\x04=\x19G\x021:\x1C."\x01*\x19&\x18';\x15-5N8[\x10\t<\x19\x15=7?)S9(\x10\x002 \x151<\x12\x14. \x01C[;\t'\f>\x02\x13Q\x10/=8' OV`;
const first = 'C';

function generateRandomArray() {
  const arr = [];
  arr[0] = Math.floor(Math.random() * 1234);

  for (let i = 1; i < 10; i++) 
      arr[i] = arr[i - 1] + 1 + Math.floor(Math.random() * ((10000 - 654*(10-i)) - arr[i - 1] - 1));
  
  arr[10] = 10001 + Math.floor(Math.random() * 500);
  for (let i = 11; i < 30; i++)
      arr[i] = arr[i - 1] + 1 + Math.floor(Math.random() * 1000);

  return arr;
}

function make() {
  // animations
  let mod = window.counter % 200;
  if (0 < mod && mod <= 100) document.getElementById('rrlogo')
    .style.opacity = ((100 - mod) * 0.8 + 20) + '%';
  else if (100 < mod && mod <= 200) document.getElementById('rrlogo')
    .style.opacity = ((mod - 100) * 0.8 + 20) + '%';

  // If clicked more than 10000 times?
  if (10000 < window.counter) {
    if (cipher[0] != first)
      alert(_______(`:,%3>,:\n55\x05\x079\x0F!*;\x03\x1FP=53;<\x00H\x1B?\x00).\x1657D7\x11=\x183(&G43'\x1A>\x10\b)#\x126\x01>Q\nR>X)1?\x01\x10^1\b'\b!\x00H\n<[=1:%3\x19!/)S=\x1C*\x0037?/#,>*0?G\x02>5J\x07>*\x1B\x16\x149&\x024\b'\x06>\x049X6Y\x04!?2+:9\x12\x07\x16;[)\x1A:\x1B<:#\x10!$9\x01KZ\x12%\x1D\x1C;->%>\x01"\f86\x15\x009Y=U;:""=\x1B7\x0F;\x12)\x168\x02&\x066\b\x15\x1D),)V'(*\x0F8#\x19\x13;[!\x02"\x1269(";\f;:>\x17;>:'>\t#"%\x01%/\x13/>\x01:#\x15X:*\x17N=<\x18>>\x19BY:<@\x15?/5\\>\v\x1D\x065*5\t;\x1C5&*0\x15-:\x12@\x18=\x01\x14\x024$+"<+)0#(G\x1124<\x030\x039Q<\x03"\x11?\x1B\x15\x13)-)T:[\x00\x0093\x19\x0F2/%8#\x01>[7'K\b`));

    document.getElementById('rrlogo').classList.add('tada');

    let ctx = document.querySelector("canvas").getContext("2d");
    let dashLen = 220;
    let dashOffset = dashLen;
    let speed = 20;
    let x = 35;
    let i = 0;
    let txt = cipher;

    ctx.font = "50px Comic Sans MS, cursive, TSCu_Comic, sans-serif"; 
    ctx.lineWidth = 5; ctx.lineJoin = "round"; ctx.globalAlpha = 2/3;
    ctx.strokeStyle = ctx.fillStyle = "#1f2f90";

    (function loop() {
      ctx.clearRect(x, 0, 60, 150);
      ctx.setLineDash([dashLen - dashOffset, dashOffset - speed]);
      dashOffset -= speed;                                        
      ctx.strokeText(txt[i], x, 90);                              

      if (dashOffset > 0) requestAnimationFrame(loop);            
      else {
        ctx.fillText(txt[i], x, 90);                              
        dashOffset = dashLen;                                     
        x += ctx.measureText(txt[i++]).width + ctx.lineWidth * Math.random();
        ctx.setTransform(1, 0, 0, 1, 0, 3 * Math.random());       
        ctx.rotate(Math.random() * 0.005);                        
        if (i < txt.length) requestAnimationFrame(loop);
      }
    })();
  }
  else {
    document.getElementById('clicks').textContent = 10000 - window.counter;
  }
}

const randomValues = generateRandomArray();
console.log(randomValues);

document.addEventListener("DOMContentLoaded", function() {
  document.getElementById('rrlogo').addEventListener('click', function() {
    window.counter += 1;
    make();
    alert(`You tried to open the gate ${window.counter} time${window.counter === 1 ? "" : "s"}!`);

    // If ~ If ~ If ~ If ~~~
    // You don't want to get hints here... do you?
    // Good Luck :)
    //
    // - by Karu
    if (window.counter == randomValues[0]) cipher = _____(cipher, ______________);
    if (window.counter == randomValues[14]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[24]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[2]) cipher = _____(cipher, _____________);
    if (window.counter == randomValues[27]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[28]) cipher = _____(cipher, ___________);
    if (window.counter == randomValues[4]) cipher = _____(cipher, ____________);
    if (window.counter == randomValues[18]) cipher = _____(cipher, ___________);
    if (window.counter == randomValues[9]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[6]) cipher = _____(cipher, ___________);
    if (window.counter == randomValues[8]) cipher = _____(cipher, __________);
    if (window.counter == randomValues[3]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[7]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[5]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[11]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[21]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[12]) cipher = _____(cipher, ___________);
    if (window.counter == randomValues[17]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[13]) cipher = _____(cipher, __________);
    if (window.counter == randomValues[19]) cipher = _____(cipher, __________);
    if (window.counter == randomValues[15]) cipher = _____(cipher, ___________);
    if (window.counter == randomValues[1]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[10]) cipher = _____(cipher, ____________);
    if (window.counter == randomValues[25]) cipher = _____(cipher, ____________);
    if (window.counter == randomValues[23]) cipher = _____(cipher, _____________);
    if (window.counter == randomValues[20]) cipher = _____(cipher, _____________);
    if (window.counter == randomValues[29]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[22]) cipher = _______________(cipher, 1);
    if (window.counter == randomValues[16]) cipher = _____(cipher, __________);
    if (window.counter == randomValues[26]) cipher = _____(cipher, ___________);
  });
});
```

여기서 처음에 `window.counter` 를 `9999` 로 변경한 후, 클릭을 시도했더니 `꼼수를 쓰지 마시오.` 라는 alert가 발생함.

그래서 10000번 request를 보내는 파이썬 코드를 작성:

```python
# solution 1

# pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert

url = "https://cau-cpss.github.io/ComputerNetwork/danger/rollingress.html"

# 크롬 드라이버 자동 종료 방지 옵션 추가
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬 드라이버 객체 생성 후 해당 URL 요청
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# 10000번 클릭 반복
for _ in range(10_000):
    driver.find_element("id", "rrlogo").click()
    # alert 확인 버튼 클릭 자동화
    alert = Alert(driver)
    alert.accept()
```

![1번](./images/1.png)

위의 코드를 수행했더니, 위와 같은 이미지가 생성되며 해결됨.

## 2번
https://cau-cpss.github.io/ComputerNetwork/ 페이지의 HTML 코드를 확인하면 아래와 같은 코드를 확인할 수 있음

```html
<!-- Hint of SecretQuestion_2  -->
<img src="images/SecretQuestion_2.png" alt="" style="display: none;">
<script type="module" src="assets/js/crypt.js"></script>
<script type="module" src="assets/js/cookie.js"></script>
```

그래서 https://cau-cpss.github.io/ComputerNetwork/images/SecretQuestion_2.png 이미지를 클릭하면 문제가 나오는데,

수치적 최적화 방법으로 해결하였음.

2번 문제를 풀 때, 수치적 최적화 알고리즘을 사용할 수 있음.

GPT로 검색해본 결과, 비선형 방정식을 풀 때 "뉴턴-랩슨 방법" 알고리즘으로 해결할 수 있었다.

저는 파이썬 코드로 작성하였는데, `scipy` 모듈의 `fsolve` 함수를 사용해서 해결.

해당 함수를 사용하면 비선형 방정식을 풀 수 있음.

해당 함수를 사용하면 뉴턴-랩슨 방법을 자동으로 수행하므로, 자코비안 행렬을 직접 계산할 필요가 없음.

```python

# solution 2
# pip install scipy
from scipy.optimize import fsolve

# 수식 정의
def equations(vars):
    x, y, z = vars
    eq1 = x / (y + z) + y / (x + z) + z / (x + y) - 4  # 원래 주어진 수식
    eq2 = x - y - 1  # x와 y가 1 차이 난다고 가정한 추가 방정식
    eq3 = y - z - 1  # y와 z가 1 차이 난다고 가정한 추가 방정식
    return [eq1, eq2, eq3]

# 초기 추정값 설정
initial_guess = [1.0, 2.0, 3.0]  # x, y, z에 대한 초기 추정값

# fsolve로 방정식 풀기
solution = fsolve(equations, initial_guess)

# 결과 출력
# Solution found: x = 0.258380151290432, y = -0.741619848709568, z = -1.741619848709568
print(f"Solution found: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")


# 검산
x = 0.258380151290432
y = -0.741619848709568
z = -1.741619848709568

result = x/(y+z)+y/(x+z)+z/(x+y)
print(result) # 4.0 근사치가 나옴

```

## 3번
아까 2번 풀때 HTML 코드를 확인했던 것 중에서 `cookie.js` 가 수상해보여서 클릭했더니, 아래와 같은 코드를 확인함.

```javascript
import { _______ } from './crypt.js';

document.cookie = `cookie=${_______(`9\x10\x03\x0F4Y\x14Z=\x16BY4\x11\x00.?)\v\x0F>";\x05:\x03)\x17;\f5 *\v3\x05%\x01=\x18?\x07*\x01=6#\x1A=\x1F\x07\b9\x02\x10\x04=\x19G\x02199N"\x00>\x18:\x1B3Y"\x00\x1FS3\x01\x1C-?\x16(,>/)S9Z2\\6"+&>\x10A\x005\x11\x1F=>\t7\x03:*\x1B\x16\x17\f&[4\b+\x05:\x04)R8Y"19\v+\x13=\x02D\r?\x13\x07\\>\x067$#+1,9\x01\x14&!\tF\x1C;\x115\x16>?2[2\f\x05\x00:\x1F\x17U8\x02:>?\x1B4_",\x131:)"\x18>53R)+5\x0F1?\x18\x1F(\x16\x01X;=9\x04=\x125$8\b7<;<A\x10?8\x00\x189\x1B;\x1A%\x11%\x1B\x10.\x00G43\x15X<\x11%\x1B <\x10X64\x1D\x12>\x04\x03,?\x125\r;\v7&;,\x1F\r;\x12\x07-\x15\b?\x0F9,9R=\f:Z>\t'-#\x01\x14-5\x01\x00\x0F?%0\x01=\x12\x17\v8(\x10\v7\x1B3\b"\x03\x13\x1B6)"\x1F9\v'\x11"ZH'9Z>Z7\x16\n<<::Q<\x11G%5"\x11\x110+=$\x17\x116:35J>:\x01\x1BJ8.:=>\v(,=\x11)\x0309\v\x0764+\x06<)\x03);(2%72\x15\x05>;\x00.`)}; path=/; expires=Fri, 31 Dec 9999 23:59:59 GMT`;
```

콘솔에 `document.cookie` 를 출력해보니, 아래와 같은 메시지가 출력됨:

```
'cookie=SecretQuestion_3: In fact, answer to question_2 is your name and the expected midterm score.'
```

