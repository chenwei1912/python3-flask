function change_st(obj)
{
    var l = document.getElementById("navbar_left").getElementsByTagName("li");
    for(var i = 0; i < l.length; i++)
    {
        l[i].className="";
    }
    obj.className="active";
}

var curRow = 1; //全局行号
var curRowId; //选中行的记录信息的ID
var curColor;

function selectRow(tr)
{
    if (curRow)
    {
        curRow.bgColor = curColor;
        curColor = tr.bgColor;
        tr.bgColor = "#FFE9B3";
    }
    else
    {
        curColor = tr.bgColor;
        tr.bgColor = "FFE9B3";
    }
    curRow = tr;
    curRowId = tr.cells[1].innerText;
    //alert(tr.cells[0].innerText);
    //alert(curRowId);

    var url_del = "user_delete/" + curRowId;
    $('#btn_del').attr('href', url_del);

    var url_upd = "user_update/" + curRowId;
    $('#btn_upd').attr('href', url_upd);
}
/*
function changeActiveRow(obj)
{ 
    if(currentActiveRow)
        currentActiveRow.style.backgroundColor="";

    currentActiveRow=obj; 
    currentActiveRow.style.backgroundColor="Red"; 
    alert(currentActiveRow.cells[0].innerHTML);
    alert(currentActiveRow.cells[1].innerHTML);
}*/

function userDelete()
{
    if (curRowId == undefined)
    {
        alert("请选择一个用户");
    }
    else
    {
        //var newHref = sprintf("{{url_for('user_delete', id='%d')}}", curRowId);
        //alert(newHref);
        //$('#btn_del').attr('href', newHref);

        var url_del = "user_delete/" + curRowId;
        //alert(url_del);
        $.get(url_del);
        
        //var url_del = "{{ url_for('user_delete', id=curRowId) }}";
        //alert(url_del);
        
        //$.get("{{ url_for('user_delete') }}", {id:curRowId});
    }
}
