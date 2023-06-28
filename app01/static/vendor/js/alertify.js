!function () {
    function f() {
        var e = {
            parent: document.body,
            version: "1.0.11",
            defaultOkLabel: "Ok",
            okLabel: "Ok",
            defaultCancelLabel: "Cancel",
            cancelLabel: "Cancel",
            defaultMaxLogItems: 2,
            maxLogItems: 2,
            promptValue: "",
            promptPlaceholder: "",
            closeLogOnClick: !1,
            closeLogOnClickDefault: !1,
            delay: 5000,
            defaultDelay: 5000,
            logContainerClass: "alertify-logs",
            logContainerDefaultClass: "alertify-logs",
            dialogs: {
                buttons: {
                    holder: "<nav>{{buttons}}</nav>",
                    ok: "<button class='ok' tabindex='1'>{{ok}}</button>",
                    cancel: "<button class='cancel' tabindex='2'>{{cancel}}</button>"
                },
                input: "<input type='text'>",
                message: "<p class='msg'>{{message}}</p>",
                log: "<div class='{{class}}'>{{message}}</div>"
            },
            defaultDialogs: {
                buttons: {
                    holder: "<nav>{{buttons}}</nav>",
                    ok: "<button class='ok' tabindex='1'>{{ok}}</button>",
                    cancel: "<button class='cancel' tabindex='2'>{{cancel}}</button>"
                },
                input: "<input type='text'>",
                message: "<p class='msg'>{{message}}</p>",
                log: "<div class='{{class}}'>{{message}}</div>"
            },
            build: function (i) {
                var g = this.dialogs.buttons.ok,
                    h = "<div class='dialog'><div>" + this.dialogs.message.replace("{{message}}", i.message);
                return "confirm" !== i.type && "prompt" !== i.type || (g = this.dialogs.buttons.cancel + this.dialogs.buttons.ok), "prompt" === i.type && (h += this.dialogs.input), h = (h + this.dialogs.buttons.holder + "</div></div>").replace("{{buttons}}", g).replace("{{ok}}", this.okLabel).replace("{{cancel}}", this.cancelLabel)
            },
            setCloseLogOnClick: function (g) {
                this.closeLogOnClick = !!g
            },
            close: function (h, g) {
                this.closeLogOnClick && h.addEventListener("click", function () {
                    d(h)
                }), g = g && !isNaN(+g) ? +g : this.delay, 0 > g ? d(h) : g > 0 && setTimeout(function () {
                    d(h)
                }, g)
            },
            dialog: function (j, g, i, h) {
                return this.setup({type: g, message: j, onOkay: i, onCancel: h})
            },
            log: function (q, h, p) {
                var m = document.querySelectorAll(".alertify-logs > div");
                if (m) {
                    var j = m.length - this.maxLogItems;
                    if (j >= 0) {
                        for (var g = 0, k = j + 1; k > g; g++) {
                            this.close(m[g], -1)
                        }
                    }
                }
                this.notify(q, h, p)
            },
            setLogPosition: function (g) {
                this.logContainerClass = "alertify-logs " + g
            },
            setupLogContainer: function () {
                var h = document.querySelector(".alertify-logs"), g = this.logContainerClass;
                return h || (h = document.createElement("div"), h.className = g, this.parent.appendChild(h)), h.className !== g && (h.className = g), h
            },
            notify: function (h, l, k) {
                var j = this.setupLogContainer(), g = document.createElement("div");
                g.className = l || "default", e.logTemplateMethod ? g.innerHTML = e.logTemplateMethod(h) : g.innerHTML = h, "function" == typeof k && g.addEventListener("click", k), j.appendChild(g), setTimeout(function () {
                    g.className += " show"
                }, 10), this.close(g, this.delay)
            },
            setup: function (q) {
                function h(i) {
                    "function" != typeof i && (i = function () {
                    }), j && j.addEventListener("click", function (l) {
                        q.onOkay && "function" == typeof q.onOkay && (k ? q.onOkay(k.value, l) : q.onOkay(l)), i(k ? {
                            buttonClicked: "ok",
                            inputValue: k.value,
                            event: l
                        } : {buttonClicked: "ok", event: l}), d(m)
                    }), g && g.addEventListener("click", function (l) {
                        q.onCancel && "function" == typeof q.onCancel && q.onCancel(l), i({
                            buttonClicked: "cancel",
                            event: l
                        }), d(m)
                    }), k && k.addEventListener("keyup", function (l) {
                        13 === l.which && j.click()
                    })
                }

                var m = document.createElement("div");
                m.className = "alertify hide", m.innerHTML = this.build(q);
                var j = m.querySelector(".ok"), g = m.querySelector(".cancel"), k = m.querySelector("input"),
                    p = m.querySelector("label");
                k && ("string" == typeof this.promptPlaceholder && (p ? p.textContent = this.promptPlaceholder : k.placeholder = this.promptPlaceholder), "string" == typeof this.promptValue && (k.value = this.promptValue));
                var o;
                return "function" == typeof Promise ? o = new Promise(h) : h(), this.parent.appendChild(m), setTimeout(function () {
                    m.classList.remove("hide"), k && q.type && "prompt" === q.type ? (k.select(), k.focus()) : j && j.focus()
                }, 100), o
            },
            okBtn: function (g) {
                return this.okLabel = g, this
            },
            setDelay: function (g) {
                return g = g || 0, this.delay = isNaN(g) ? this.defaultDelay : parseInt(g, 10), this
            },
            cancelBtn: function (g) {
                return this.cancelLabel = g, this
            },
            setMaxLogItems: function (g) {
                this.maxLogItems = parseInt(g || this.defaultMaxLogItems)
            },
            theme: function (g) {
                switch (g.toLowerCase()) {
                    case"bootstrap":
                        this.dialogs.buttons.ok = "<button class='ok btn btn-primary' tabindex='1'>{{ok}}</button>", this.dialogs.buttons.cancel = "<button class='cancel btn btn-default' tabindex='2'>{{cancel}}</button>", this.dialogs.input = "<input type='text' class='form-control'>";
                        break;
                    case"purecss":
                        this.dialogs.buttons.ok = "<button class='ok pure-button' tabindex='1'>{{ok}}</button>", this.dialogs.buttons.cancel = "<button class='cancel pure-button' tabindex='2'>{{cancel}}</button>";
                        break;
                    case"mdl":
                    case"material-design-light":
                        this.dialogs.buttons.ok = "<button class='ok mdl-button mdl-js-button mdl-js-ripple-effect'  tabindex='1'>{{ok}}</button>", this.dialogs.buttons.cancel = "<button class='cancel mdl-button mdl-js-button mdl-js-ripple-effect' tabindex='2'>{{cancel}}</button>", this.dialogs.input = "<div class='mdl-textfield mdl-js-textfield'><input class='mdl-textfield__input'><label class='md-textfield__label'></label></div>";
                        break;
                    case"angular-material":
                        this.dialogs.buttons.ok = "<button class='ok md-primary md-button' tabindex='1'>{{ok}}</button>", this.dialogs.buttons.cancel = "<button class='cancel md-button' tabindex='2'>{{cancel}}</button>", this.dialogs.input = "<div layout='column'><md-input-container md-no-float><input type='text'></md-input-container></div>";
                        break;
                    case"default":
                    default:
                        this.dialogs.buttons.ok = this.defaultDialogs.buttons.ok, this.dialogs.buttons.cancel = this.defaultDialogs.buttons.cancel, this.dialogs.input = this.defaultDialogs.input
                }
            },
            reset: function () {
                this.parent = document.body, this.theme("default"), this.okBtn(this.defaultOkLabel), this.cancelBtn(this.defaultCancelLabel), this.setMaxLogItems(), this.promptValue = "", this.promptPlaceholder = "", this.delay = this.defaultDelay, this.setCloseLogOnClick(this.closeLogOnClickDefault), this.setLogPosition("bottom left"), this.logTemplateMethod = null
            },
            injectCSS: function () {
                if (!document.querySelector("#alertifyCSS")) {
                    var h = document.getElementsByTagName("head")[0], g = document.createElement("style");
                    g.type = "text/css", g.id = "alertifyCSS", g.innerHTML = ".alertify-logs>*{padding:12px 24px;color:#fff;box-shadow:0 2px 5px 0 rgba(0,0,0,.2);border-radius:1px}.alertify-logs>*,.alertify-logs>.default{background:rgba(0,0,0,.8)}.alertify-logs>.error{background:rgba(244,67,54,.8)}.alertify-logs>.success{background:rgba(76,175,80,.9)}.alertify{position:fixed;background-color:rgba(0,0,0,.3);left:0;right:0;top:0;bottom:0;width:100%;height:100%;z-index:1}.alertify.hide{opacity:0;pointer-events:none}.alertify,.alertify.show{box-sizing:border-box;transition:all .33s cubic-bezier(.25,.8,.25,1)}.alertify,.alertify *{box-sizing:border-box}.alertify .dialog{padding:12px}.alertify .alert,.alertify .dialog{width:100%;margin:0 auto;position:relative;top:50%;transform:translateY(-50%)}.alertify .alert>*,.alertify .dialog>*{width:400px;max-width:95%;margin:0 auto;text-align:center;padding:12px;background:#fff;box-shadow:0 2px 4px -1px rgba(0,0,0,.14),0 4px 5px 0 rgba(0,0,0,.098),0 1px 10px 0 rgba(0,0,0,.084)}.alertify .alert .msg,.alertify .dialog .msg{padding:12px;margin-bottom:12px;margin:0;text-align:left}.alertify .alert input:not(.form-control),.alertify .dialog input:not(.form-control){margin-bottom:15px;width:100%;font-size:100%;padding:12px}.alertify .alert input:not(.form-control):focus,.alertify .dialog input:not(.form-control):focus{outline-offset:-2px}.alertify .alert nav,.alertify .dialog nav{text-align:right}.alertify .alert nav button:not(.btn):not(.pure-button):not(.md-button):not(.mdl-button),.alertify .dialog nav button:not(.btn):not(.pure-button):not(.md-button):not(.mdl-button){background:transparent;box-sizing:border-box;color:rgba(0,0,0,.87);position:relative;outline:0;border:0;display:inline-block;-ms-flex-align:center;-ms-grid-row-align:center;align-items:center;padding:0 6px;margin:6px 8px;line-height:36px;min-height:36px;white-space:nowrap;min-width:88px;text-align:center;text-transform:uppercase;font-size:14px;text-decoration:none;cursor:pointer;border:1px solid transparent;border-radius:2px}.alertify .alert nav button:not(.btn):not(.pure-button):not(.md-button):not(.mdl-button):active,.alertify .alert nav button:not(.btn):not(.pure-button):not(.md-button):not(.mdl-button):hover,.alertify .dialog nav button:not(.btn):not(.pure-button):not(.md-button):not(.mdl-button):active,.alertify .dialog nav button:not(.btn):not(.pure-button):not(.md-button):not(.mdl-button):hover{background-color:rgba(0,0,0,.05)}.alertify .alert nav button:not(.btn):not(.pure-button):not(.md-button):not(.mdl-button):focus,.alertify .dialog nav button:not(.btn):not(.pure-button):not(.md-button):not(.mdl-button):focus{border:1px solid rgba(0,0,0,.1)}.alertify .alert nav button.btn,.alertify .dialog nav button.btn{margin:6px 4px}.alertify-logs{position:fixed;z-index:1}.alertify-logs.bottom,.alertify-logs:not(.top){bottom:16px}.alertify-logs.left,.alertify-logs:not(.right){left:16px}.alertify-logs.left>*,.alertify-logs:not(.right)>*{float:left;transform:translateZ(0);height:auto}.alertify-logs.left>.show,.alertify-logs:not(.right)>.show{left:0}.alertify-logs.left>*,.alertify-logs.left>.hide,.alertify-logs:not(.right)>*,.alertify-logs:not(.right)>.hide{left:-110%}.alertify-logs.right{right:16px}.alertify-logs.right>*{float:right;transform:translateZ(0)}.alertify-logs.right>.show{right:0;opacity:1}.alertify-logs.right>*,.alertify-logs.right>.hide{right:-110%;opacity:0}.alertify-logs.top{top:0}.alertify-logs>*{box-sizing:border-box;transition:all .4s cubic-bezier(.25,.8,.25,1);position:relative;clear:both;backface-visibility:hidden;perspective:1000;max-height:0;margin:0;padding:0;overflow:hidden;opacity:0;pointer-events:none}.alertify-logs>.show{margin-top:12px;opacity:1;max-height:1000px;padding:12px;pointer-events:auto}", h.insertBefore(g, h.firstChild)
                }
            },
            removeCSS: function () {
                var g = document.querySelector("#alertifyCSS");
                g && g.parentNode && g.parentNode.removeChild(g)
            }
        };
        return e.injectCSS(), {
            _$$alertify: e, parent: function (g) {
                e.parent = g
            }, reset: function () {
                return e.reset(), this
            }, alert: function (g, i, h) {
                return e.dialog(g, "alert", i, h) || this
            }, confirm: function (g, i, h) {
                return e.dialog(g, "confirm", i, h) || this
            }, prompt: function (g, i, h) {
                return e.dialog(g, "prompt", i, h) || this
            }, log: function (g, h) {
                return e.log(g, "default", h), this
            }, theme: function (g) {
                return e.theme(g), this
            }, success: function (g, h) {
                return e.log(g, "success", h), this
            }, error: function (g, h) {
                return e.log(g, "error", h), this
            }, cancelBtn: function (g) {
                return e.cancelBtn(g), this
            }, okBtn: function (g) {
                return e.okBtn(g), this
            }, delay: function (g) {
                return e.setDelay(g), this
            }, placeholder: function (g) {
                return e.promptPlaceholder = g, this
            }, defaultValue: function (g) {
                return e.promptValue = g, this
            }, maxLogItems: function (g) {
                return e.setMaxLogItems(g), this
            }, closeLogOnClick: function (g) {
                return e.setCloseLogOnClick(!!g), this
            }, logPosition: function (g) {
                return e.setLogPosition(g || ""), this
            }, setLogTemplate: function (g) {
                return e.logTemplateMethod = g, this
            }, clearLogs: function () {
                return e.setupLogContainer().innerHTML = "", this
            }, version: e.version
        }
    }

    var a = 500, d = function (g) {
        if (g) {
            var e = function () {
                g && g.parentNode && g.parentNode.removeChild(g)
            };
            g.classList.remove("show"), g.classList.add("hide"), g.addEventListener("transitionend", e), setTimeout(e, a)
        }
    };
    if ("undefined" != typeof module && module && module.exports) {
        module.exports = function () {
            return new f
        };
        var c = new f;
        for (var b in c) {
            module.exports[b] = c[b]
        }
    } else {
        "function" == typeof define && define.amd ? define(function () {
            return new f
        }) : window.alertify = new f
    }
}();