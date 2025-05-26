const base = {
    get() {
        return {
            url : "http://localhost:8080/django5131502w/",
            name: "django5131502w",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于爬虫的山洪信息管理系统"
        } 
    }
}
export default base
