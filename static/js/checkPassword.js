$(() => {
  const app = Vue.createApp({
    delimiters: ["{", "}"],
  });

  app.component("notice_detail", {
    template: `
<div>
    <div>
      <span class="form_category">제목</span>
      <span>{{notice.title}}</span>
    </div>
    <div>
      <span class="form_category">작성자</span>
      <span class="form_category">{{notice.author.userId}}</span>
    </div>
    <div>
      <span class="form_category">작성일</span>
      <span class="form_category">{{notice.createdAt|date:"Y-m-d"}}</span>
      <span class="form_category">조회수</span>
      <span>{{notice.watched}}</span>
    </div>
    <div></div>
    <div>
      <span class="form_category">첨부파일</span>
      {% if attach %}
      <!--  -->
      {% for file in attach %}
      <a href="/{{ file.path }}" download>{{ file.filename }}</a>
      {% endfor %}
      <!--  -->
      {% endif %}
    </div>
    <hr />
    <!-- https://parkhyeonchae.github.io/2020/04/08/django-project-21/ -->
    <!-- 글상세보기 Tag Escape 방지 -->
    <div>{{ notice.content | safe }}</div>
    <hr />
    {% if notice.author_id == request.session.user.id %}
    <div>
      <a href="/notice_update/{{notice.id}}"><button>수정</button></a>
      <button id="deleteNotice">삭제</button>
    </div>
    {% endif %}
</div>
    `,
  });

  app.mount("#notice_detail");
});
