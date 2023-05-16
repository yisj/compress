# Compress

내가 디카로 찍은 사진들을 압축하기 위해 만든 파이썬 코드

##
* `1. target` 폴더를 만들고 그 안에 폴더별로 사진을 집어 넣는다.
* `compress.py`를 실행시키면 `1. target` 폴더의 사진들이 `2. compressed`로 압축되어 옮겨진다.
* `3. selected` 폴더를 만들고 내가 선택한 사진들을 집어 넣는다.
* `original.py`를 실행시키면 `3. selected`에 압축되어 있는 사진 파일과 일치하는 원본 파일을 찾아 `4. original`에 만들어준다. 

## 폴더 구조
```
1. target
    subfolder1
    subfolder2
    ...
2. compressed
    subfolder1
    subfolder2
    ...
3. selected
    subfolder1
    subfolder2
    ...
4. original
    subfolder1
    subfolder2
    ...

```