struct NewsDetail{
1:i32 news_id,
2:string news_title,
3:string news_content,
4:string news_type,
5:string news_data
}

struct News{
1:i32 news_id,
2:string news_title,
3:string news_type,
}

service NewsServlet {
    NewsDetail get_news_detail(1:i32 news_id);
    list<News> get_news_list();
}
