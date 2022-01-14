## Feature Detection

### 코드 설명

4장의 영상(boat1, budapest1, newspaper1, s1)을 선택한 후   
Canny Edge 와 Harris Corner를 검출해서 결과 출력.

### 결과

![image](https://user-images.githubusercontent.com/79437689/149483385-2f16619a-d435-4a6e-b57d-4e63dd5b9a60.png)
![image](https://user-images.githubusercontent.com/79437689/149483747-ed9d6598-5c1d-4f69-8e32-20ec2e6c593b.png)

## Matching

### 코드 설명

영상셋(boat, budapest, newspaper, s1~2)에서 두 장을 선택하여 SIFT, SURF, ORB 를 추출하고   
Matching 알고리즘을 통해 두 영상을 하나의 영상으로 Warping 하는 결과 출력.

### 결과

![image](https://user-images.githubusercontent.com/79437689/149484146-dcf21b0c-3e87-4d79-bf1a-95fe67151d17.png)
![image](https://user-images.githubusercontent.com/79437689/149484896-ff056862-f20b-41a7-8213-16302d3f1a1d.png)
![image](https://user-images.githubusercontent.com/79437689/149485010-0ffa9452-b5fc-4102-a2b8-1d50cd0c0bbe.png)

## Panorama

### 코드 설명

CreaterStitcher 를 이용하여 4개의 영상셋을 하나의 Panorama 영상으로 출력.

### 결과

![image](https://user-images.githubusercontent.com/79437689/149485392-23a199cc-ae59-47f5-9bbe-d8d477dc958c.png)

## Optical Flow

### 코드 설명

두 사진을 이용하여 Good Feature to Tracking 을 추출하고   
Pyramid Lucas-Kanade 알고리즘을 적용한 영상 출력.   
Farneback 과 DualTVL1 Optical Flow 를 적용한 영상 출력.

### 결과

![image](https://user-images.githubusercontent.com/79437689/149485890-e5495cf0-0636-4773-bec3-6860d8fb3cdf.png)
![image](https://user-images.githubusercontent.com/79437689/149486005-a4de7384-cf6a-4478-b8c3-c63d09173b1d.png)
![image](https://user-images.githubusercontent.com/79437689/149486132-999735f3-d599-4560-9d63-1bc73f2bac3c.png)

