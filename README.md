# study
Updating the code I wrote while studying.

이 저장소는 알고리즘 및 프로그래밍 학습을 진행하며 작성한 코드들을 보관하는 공간입니다. 
여러 프로그래밍 언어를 사용하여 같은 문제를 해결해 보며, 각 언어의 특징과 장단점을 비교하고 학습합니다.

## 🗂️ Directory Structure

IDE의 완벽한 환경 지원(자동완성, 디버깅, 린팅 등)과 패키지 관리의 독립성을 위해, 저장소는 **언어 중심(Language-centric)**으로 분리되어 있습니다. 

```text
study/
├── python/              # Python 풀이 공간
│   ├── pyproject.toml   # 패키지 및 린터(Ruff) 등 환경 설정
│   ├── 001_Two_Sum.py
│   └── ...
├── go/                  # Go 풀이 공간
│   ├── go.mod           # Go 모듈 설정
│   ├── 001_Two_Sum/
│   │   └── main.go
│   └── ...
└── kotlin/              # Kotlin 풀이 공간
    ├── build.gradle.kts # Gradle 빌드 및 환경 설정
    └── src/main/kotlin/
        ├── TwoSum.kt
        └── ...

```

## 🔍 How to Navigate

* **독립된 환경:** 각 언어 폴더(`python/`, `go/`, `kotlin/`)는 완전히 독립적인 프로젝트처럼 동작합니다. 개발 시 해당 언어의 루트 폴더를 IDE에서 열거나(Open Project), 워크스페이스에 추가하여 작업하는 것을 권장합니다.
* **코드 검색 및 비교:** 서로 다른 언어로 작성된 동일한 문제의 코드를 비교할 때는 파일 탐색기 대신 에디터의 파일 검색 기능(`Ctrl+P` 또는 `Cmd+P`)을 사용하여 문제 번호(예: `001`)를 검색하면 빠르게 넘나들 수 있습니다.

## ⚙️ Environments & Tools

* **Python**: `pre-commit`과 `Ruff`를 사용하여 코드 스타일 일관성을 유지합니다.
* **Go**: Go 표준 도구(`gofmt`)를 활용합니다.
* **Kotlin**: Gradle 기반으로 빌드 및 실행을 관리합니다.

```

---

README 파일이 깔끔하게 준비되었네요. 

다음 단계로 파이썬 환경 세팅을 마무리하기 위해, `python/` 폴더 안에 들어갈 **`pyproject.toml` (Ruff 설정 포함) 파일 내용**을 작성해 드릴까요? 필요하시다면 `pre-commit` 설정 파일도 옵션 B 구조에 맞게 경로를 수정해 드리겠습니다.

```