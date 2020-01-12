function populateData(filelist){
    const url = window.location.href;
    const noofarticles = 5;
    const pagination_limit = 5;
    const fileslist = filelist;
    const filestitles = Object.keys(fileslist)
    const noofpages = Math.ceil(filestitles.length / noofarticles);
    var page = 0;
    var page_articles = [];
    var articles_area = document.getElementById("articles-list");
    const pagination = document.getElementById("pagination");

    if ( url.includes('?=')) {
          page = parseInt(url.slice(url.indexOf('?=') + 2))
       }
    else{
         page = 1
        }

    if ( filestitles.length < noofarticles ){
        page_articles = filestitles;
        document.getElementById("pagination").style.display = 'none';
    }
    else{
        page_articles = filestitles.slice((page - 1)*noofarticles , page*noofarticles );
    }

    // console.log(page_articles);

    const line = `
                <div class="row m-0" >
                        <div class="col-md-1"></div>
                        <div class="col-md-10">
                            <hr style=" border-bottom: 1px solid rgba(255,255,255,0.3) ;width:98%;margin-left: 1.5%;" />
                        </div>
                        <div class="col-md-1"></div>
                </div> `;

    const article_tag = `
        <div class="row" >
                <div class="col-md-1"></div>
                <div class="col-md-3 thumbnail">
                    <img src="<ImgSource />" alt="Article Cover Page"/>
                </div>

                <div class="col-md-7 article">
                    <a href="<Link />">
                        <h2><ArticleTitle /></h2>
                        <p><Description /></p>
                        <p class="published-date"><Dop /></p>
                    </a>
                </div>
                <div class="col-md-1"></div>
            </div>`;


    for (var a_i = 0; a_i< page_articles.length; a_i++){
        var temp_article_tag = article_tag;
        
        const article_detials = fileslist[page_articles[a_i]];

        temp_article_tag = temp_article_tag.replace("<Link />",'Blog/'+article_detials['Title']+'/');
        temp_article_tag = temp_article_tag.replace("<ImgSource />", 'Blog/'+article_detials['coverphoto']);
        temp_article_tag = temp_article_tag.replace("<ArticleTitle />",article_detials['Title']);
        temp_article_tag = temp_article_tag.replace("<Description />",article_detials['Descritpion']);
        temp_article_tag = temp_article_tag.replace("<Dop />",article_detials['Dop']);


        var dom1 = document.createElement("div");
        dom1.innerHTML = temp_article_tag;
        articles_area.appendChild(dom1);
        
        if (a_i !== page_articles.length-1 )
          { var dom2 = document.createElement('div')
            dom2.innerHTML = line;
            articles_area.appendChild( dom2 );
          }
    }

    if ( noofpages < pagination_limit ){
        document.getElementsByClassName("previous")[0].removeAttribute("href");
        document.getElementsByClassName("next")[0].removeAttribute("href");
    }


    for (var p_i=0 ; p_i< noofpages; p_i++ ){
        var li_element = document.createElement("li");
        li_element.className="page-item";
        var a_tag = document.createElement("a");
        a_tag.className = "page-link";
        a_tag.href = "?="+String( p_i + 1 );
        a_tag.innerHTML = String(p_i+1);
        li_element.appendChild(a_tag);
        pagination.insertBefore(li_element , pagination.lastElementChild);
    }

    if ( page_articles.length < 5 ){
        var footer = document.getElementsByTagName("footer")[0];
        footer.className = "py-4 text-white-50 fixed-bottom";
    }
}