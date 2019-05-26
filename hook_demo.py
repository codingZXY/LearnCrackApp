import frida,sys

jscode = """
Java.perform(function(){
    var hook_cls = Java.use('com.example.myapplication.MainActivity')
    hook_cls.check.implementation = function(a,b){
        console.log("Hook Start...");
        send(arguments);
        a = "ethan";
        b = "1234";
        send("Success!");
        return this.check(a,b);
    }
}
);
"""

def message(message,data):
    if message["type"] == 'send':
        print("[*] {0}".format(message["payload"]))
    else:
        print(message)

process = frida.get_remote_device().attach('com.example.myapplication')
script = process.create_script(jscode)
script.on("message",message)
script.load()
sys.stdin.read()