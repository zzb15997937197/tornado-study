$(document).ready(function() {                      //页面加载完成后调用
if (! window.console) window.console = {};
if (! window.console.log) window.console.log = function() {};
//重新定义发送表单" messageform"的submit事件
$("#messageform").live("submit", function(e) {
        newMessage($(this));
        return false;
});
//定义发送表单" messageform"的keypress事件，使用户在按下回车键时自动发送
$("#messageform").live("keypress", function(e) {
    //回车键的keyCode为13
    if (e.keyCode == 13) {
        newMessage($(this));
    return false;      }});
$("#message").select();
//将页面的焦点设置在message控件上
updater.start();
//调用updater.start()
});
function newMessage(form) {
    var message = form.formToDict();
    //调用jQuery.fn.formToDict
    updater.socket.send(JSON.stringify(message));
    //生成JSON字符串
    console.log("发送消息:",message)
    form.find("input[type=text]").val("").select();
    }
jQuery.fn.formToDict = function() {
    //将表单中的所有输入值保存到JSON对象中
        var fields = this.serializeArray();
        var json = {}
        for (var i = 0; i < fields.length; i++) {
                json[fields[i].name] = fields[i].value;
        }

        if (json.next) delete json.next;
        return json;
};

var updater = {
    socket: null,
    start: function() {
    var url = "ws://" + location.host + "/chat_socket" //服务器WebSocket的地址
    console.log("websocket地址:",url)
    updater.socket = new WebSocket(url);               //用WebSocket连接服务器
    //定义收到Websocket消息时的行为，即调用showMessage()函数
    updater.socket.onmessage = function(event) {
            updater.showMessage(JSON.parse(event.data));
      }
    },

    showMessage: function(message) {
        //将收到的信息显示在页面上
        var node = $(message.html);
        node.hide();
        $("#inbox").append(node);
        //添加在inbox标签的尾部
        node.slideDown();
        //窗口滑到底部
        }
};