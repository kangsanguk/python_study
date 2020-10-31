#1. 영화 추가
#티켓 가겨 모두 동일
#arFilm =[]
#청소년 관람 불가 영화제목 앞에 ●를 붙여준다
#2. 상품 추가
#상품 가격 모두 상이
#arName = []
#arPrice = []

title = "CGV\n"
msg = "1. 영화관리\n2.상품관리\n3.나가기\n"
err_msg = "다시 시도해주세요"
choice = 0

#영화
film_msg = "1.영화 추가\n2.영화 수정\n3.영화 검색\n4.영화 삭제\n5.영화 목록\n6.메인메뉴로 이동\n"
insert_msg = "1.전체 이용가\n2.청소년 관람 불가\n3.취소\n"
film_search_msg = "영화 제목 검색 : "
film_delete_msg = "삭제하실 영화 제목 : "
film_update_msg = "수정하실 영화 제목 : "
new_film_msg = "새로운 영화 제목: "

arFilm = []
film_result = ""

#상품
food_msg = "1.상품 추가\n2.상품 수정\n3.상품 검색\n4.상품 삭제\n5.상품 목록\n6.메인메뉴로 이동\n"

arName = []
arPrice = []

while True:
    choice = int(input(msg))
    #영화관리
    if choice == 1:
        while True:
            choice =  int(input(film_msg))
            
            #추가
            if choice == 1:
                choice = int(input(insert_msg))
                #전체 이용가
                if choice == 1:
                    film_result = ""
                #청소년 관람 불가
                elif choice == 2:
                    #청불영화는 ●로 영화 제목 앞에 표시해준다.
                    film_result = "●"
                elif choice == 3:
                    #밑에서 일괄처리를 하기 때문에 정상적인 선택이 아니라면
                    #continue로 막아준다.
                    continue
                else:
                    print(err_msg)
                    continue

                temp = input("영화 제목 : ")
                #영화제목은 중복이 없어야 한다.
                #중복검사를 not in으로 한다.
                if temp not in arFilm:
                    #위에서 선택한 이용등급 표시(film_result)를
                    #입력한 영화제목(temp) 앞에 연결해준다.
                    arFilm.append(film_result + temp)
                else:
                    print("이미 등록된 영화입니다.")
                    
            #수정
            elif choice == 2:
                #Flag
                check = False
                
                temp = input(film_update_msg)
                
                for i in arFilm:
                    #i는 저장소에 있는 영화 제목을 순서대로 담는다.
                    if temp == i.replace("●", ""):
                        #만약 영화제목에 ●표시가 있다면 없애주고 비교해준다.
                        #입력할 때에는 이용등급에 상관없이 영화제목만 입력하기 때문!
                        if "●" in i:
                            #저장소에는 청불영화제목 앞에 ●표시가 붙은 채로 저장되어 있다.
                            #따라서 만약 영화제목 앞에 표시가 되어 있다면 사용자가 입력한
                            #영화제목 앞에도 표시를 붙여준다.
                            temp ="●" + temp

                        #새로운 영화의 이용등급을 먼저 선택한다.    
                        choice = int(input(insert_msg))
                        #전체이용가
                        if choice == 1:
                            film_result = ""

                        #청소년 관람 불가
                        elif choice == 2:
                            film_result = "●"

                        #새로운 영화제목을 입력받는다.
                        new = input(new_film_msg)

                        #새로운 영화제목 중복검사
                        if new not in arFilm:
                            #사용자가 처음에 입력한 수정전 영화제목을
                            #저장소에서 찾고(index(temp)) 그방에
                            #새로운 영화제목을 대입연산자로 덮어씌워준다.
                            arFilm[arFilm.index(temp)] = film_result + new
                            
                            #이 영역 밖에서 결과를 알리기 위해
                            #수정 성공시 check를 True로 바꿔준다.
                            check = True
                            
                #check가 True라면 들어가지 않고
                #check가 False라면 들어가서 오류내용을 출력한다.
                if not check:
                    print("다시 시도해주세요")
                    continue
                
            #검색
            elif choice == 3:
                #문자가 하나라도 포함되어 있다면 검색
                film_result = ''
                cnt = 0

                #검색할 영화제목을 입력한다.
                temp = input(film_search_msg)

                for i in arFilm:
                    #사용자가 입력한 키워드가 영화제목에 한개라도 포함되어 있다면
                    #검색 결과에 누적해서 담아준다.
                    if temp in i:
                          film_result += i.replace("●","[청소년 관람 불가]") + "\n"
                          #총 검색 결과 건수를 1 증가 시킨다.
                          cnt += 1
                          
                film_result += "검색 결과 총 " + str(cnt) + "건\n"

                #저장된 영화가 없거나, 검색 결과가 0개이면
                #film_result에 '검색 결과 없음'을 담아준다.
                if len(arFilm) == 0 or cnt == 0:
                    film_result = "검색 결과 없음\n"
                    
                print(film_result, end = '')
               
            
            #삭제
            elif choice == 4:
                check = False
                
                #삭제할 영화제목을 입력받는다.
                temp = int(input(film_delete_msg))
                for i in arFilm:
                    #i는 저장소에 있는 영화제목을 순서대로 저장한다.
                    if temp == i.replace("●",""):
                        check = True
                        if "●" in i:
                            temp = "●" + temp

                        #영화제목이 중복이 없으므로 remove(값)로 삭제한다.    
                        arFilm.remove(temp)
                        #사용자에게는 ●표시를 보여주면 안되기 때문에
                        #원하는 메세지로 바꿔서 출력한다.
                        print(temp.replace("●", "[청소년 관람 불가]") + "삭제 성공")
                        #영화를 찾아서 삭제했다면 더 이상 반복할 필요가 없기 때문에
                        #break 해준다.
                        break
                
                if not check:
                    print(temp + "라는 영화는 존재하지 않습니다")
            
            #목록
            elif choice == 5:
                film_result = ''
                for i in arFilm:
                    #flim_result += "[청소년 관람 불가]" if "●" in i else ""
                    film_result += i.replace("●","[청소년 관람 불가]") + "\n"
                    
                if len(arFilm) == 0:
                    film_result = "검색 결과 없음\n"
                    
                print(film_result, end = '')
                
            #메인메뉴
            elif choice == 6:
                break
            else:
                print(err_msg)
                
    #상품 관리
    elif choice == 2:
         while True:
            choice =  int(input(food_msg))
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                break
            else:
                print(err_msg)
        
