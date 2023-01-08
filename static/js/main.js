$( document ).ready(function() {

    $( "input:image").click(function(){
        div_elem=$(this).parent();
        label=div_elem.children()[0]
        elem=label.textContent.trim();
        console.log(elem);
        $.ajax({
            type:"DELETE",
            url:'http://localhost:8000/api/todoItem/'+elem+'/delete/',
            success: function(response) {
                console.log(div_elem);

                div_elem.parent().remove();
            },

        });
    });

   
    $('input.checkbox').click(function(){
        let dataToSend={};
        var $element = $(this);
        console.log($element);
        var parentElem = $(this).parent();
        parentTagName = parentElem.get(0).tagName.toLowerCase();
        if(parentTagName == "label") {
            label = parentElem;
        }
        
        lableHtml=label.html();
        title=lableHtml.split('>')[1].split('<')[0];
        title = title.trim();
        console.log(title);
        if($element.is(":checked")==true)
        {
            dataToSend={
                'title':title,
                'is_completed':true
            };
            $.ajax({
                type:"GET",
                url:'http://localhost:8000',
                
                success: function(response) {
                    label.addClass('completed');
                    console.log(response);
                },
            });
        }
        else{
            dataToSend={
                'title':title,
                'is_completed':false
            };
            $.ajax({
                url:'http://localhost:8000',
                
                success: function(response) {
                    label.removeClass('completed');
                    console.log(response);
                }
            });
        }
        console.log(dataToSend);
        $.ajax({
            type:"POST",
            url: 'http://localhost:8000/api/update/'+title+'/',
            data:dataToSend,
            dataType: 'json',
            success: function(resultData) {console.log(dataToSend.title +' updated')}
        });
    });  
});