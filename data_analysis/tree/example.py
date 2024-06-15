class QuestionNode:
    def __init__(self, question, options=None):
        self.question = question
        self.options = options or {}

    def ask_question(self):
        print(self.question)

    def next_node(self, response):
        return self.options.get(response)


def traverse_tree(node):
    while True:
        node.ask_question()
        response = input().strip().lower()

        if response == 'exit':
            print("프로그램을 종료합니다.")
            return

        next_node = node.next_node(response)
        if next_node:
            if isinstance(next_node, QuestionNode):
                node = next_node
            else:
                print("선택한 영화는", next_node, "입니다.")
                return
        else:
            print("유효한 응답이 아닙니다. 다시 입력하세요.")


# 질문 트리 생성
action_directors = QuestionNode("어떤 감독의 영화를 보고 싶으세요?",
                                {'christopher nolan': '인셉션', 'james cameron': '아바타'})
comedy_actors = QuestionNode("어떤 배우의 코미디 영화를 보고 싶으세요?",
                             {'jim carrey': '반지의 제왕', 'adam sandler': '클릭'})
movie_type = QuestionNode("어떤 종류의 영화를 보고 싶으세요?",
                          {'액션': action_directors, '코미디': comedy_actors})

# 질문 트리 순회
traverse_tree(movie_type)
