!function (t, e) {
    "function" == typeof define && define.amd ? define(function () {
        return e(t)
    }) : e(t)
}(this, function (c) {
    var Wj, d = function () {
        function u(t) {
            return null == t ? String(t) : V[B.call(t)] || "object"
        }

        function a(t) {
            return "function" == u(t)
        }

        function o(t) {
            return null != t && t == t.window
        }

        function s(t) {
            return null != t && t.nodeType == t.DOCUMENT_NODE
        }

        function i(t) {
            return "object" == u(t)
        }

        function l(t) {
            return i(t) && !o(t) && Object.getPrototypeOf(t) == Object.prototype
        }

        function f(t) {
            var e = !!t && "length" in t && t.length, n = x.type(t);
            return "function" != n && !o(t) && ("array" == n || 0 === e || "number" == typeof e && 0 < e && e - 1 in t)
        }

        function h(t) {
            return t.replace(/::/g, "/").replace(/([A-Z]+)([A-Z][a-z])/g, "$1_$2").replace(/([a-z\d])([A-Z])/g, "$1_$2").replace(/_/g, "-").toLowerCase()
        }

        function n(t) {
            return t in e ? e[t] : e[t] = new RegExp("(^|\\s)" + t + "(\\s|$)")
        }

        function p(t, e) {
            return "number" != typeof e || P[h(t)] ? e : e + "px"
        }

        function r(t) {
            return "children" in t ? E.call(t.children) : x.map(t.childNodes, function (t) {
                return 1 == t.nodeType ? t : void 0
            })
        }

        function d(t, e) {
            var n, r = t ? t.length : 0;
            for (n = 0; n < r; n++) this[n] = t[n];
            this.length = r, this.selector = e || ""
        }

        function v(t, e) {
            return null == e ? x(t) : x(t).filter(e)
        }

        function m(t, e, n, r) {
            return a(e) ? e.call(t, n, r) : e
        }

        function g(t, e, n) {
            null == n ? t.removeAttribute(e) : t.setAttribute(e, n)
        }

        function j(t, e) {
            var n = t.className || "", r = n && n.baseVal !== w;
            return e === w ? r ? n.baseVal : n : void (r ? n.baseVal = e : t.className = e)
        }

        function y(e) {
            try {
                return e ? "true" == e || "false" != e && ("null" == e ? null : +e + "" == e ? +e : /^[\[\{]/.test(e) ? x.parseJSON(e) : e) : e
            } catch (t) {
                return e
            }
        }

        var w, b, x, _, $, T, S = [], N = S.concat, D = S.filter, E = S.slice, k = c.document, C = {}, e = {},
            P = {"column-count": 1, columns: 1, "font-weight": 1, "line-height": 1, opacity: 1, "z-index": 1, zoom: 1},
            I = /^\s*<(\w+|!)[^>]*>/, A = /^<(\w+)\s*\/?>(?:<\/\1>|)$/,
            O = /<(?!area|br|col|embed|hr|img|input|link|meta|param)(([\w:]+)[^>]*)\/>/gi, q = /^(?:body|html)$/i,
            M = /([A-Z])/g, L = ["val", "css", "html", "text", "data", "width", "height", "offset"],
            t = k.createElement("table"), F = k.createElement("tr"),
            R = {tr: k.createElement("tbody"), tbody: t, thead: t, tfoot: t, td: F, th: F, "*": k.createElement("div")},
            Z = /complete|loaded|interactive/, z = /^[\w-]*$/, V = {}, B = V.toString, U = {},
            W = k.createElement("div"), J = {
                tabindex: "tabIndex",
                readonly: "readOnly",
                for: "htmlFor",
                class: "className",
                maxlength: "maxLength",
                cellspacing: "cellSpacing",
                cellpadding: "cellPadding",
                rowspan: "rowSpan",
                colspan: "colSpan",
                usemap: "useMap",
                frameborder: "frameBorder",
                contenteditable: "contentEditable"
            }, K = Array.isArray || function (t) {
                return t instanceof Array
            };
        return U.matches = function (t, e) {
            if (!e || !t || 1 !== t.nodeType) return !1;
            var n = t.matches || t.webkitMatchesSelector || t.mozMatchesSelector || t.oMatchesSelector || t.matchesSelector;
            if (n) return n.call(t, e);
            var r, i = t.parentNode, o = !i;
            return o && (i = W).appendChild(t), r = ~U.qsa(i, e).indexOf(t), o && W.removeChild(t), r
        }, $ = function (t) {
            return t.replace(/-+(.)?/g, function (t, e) {
                return e ? e.toUpperCase() : ""
            })
        }, T = function (n) {
            return D.call(n, function (t, e) {
                return n.indexOf(t) == e
            })
        }, U.fragment = function (t, e, n) {
            var r, i, o;
            return A.test(t) && (r = x(k.createElement(RegExp.$1))), r || (t.replace && (t = t.replace(O, "<$1></$2>")), e === w && (e = I.test(t) && RegExp.$1), e in R || (e = "*"), (o = R[e]).innerHTML = "" + t, r = x.each(E.call(o.childNodes), function () {
                o.removeChild(this)
            })), l(n) && (i = x(r), x.each(n, function (t, e) {
                -1 < L.indexOf(t) ? i[t](e) : i.attr(t, e)
            })), r
        }, U.Z = function (t, e) {
            return new d(t, e)
        }, U.isZ = function (t) {
            return t instanceof U.Z
        }, U.init = function (t, e) {
            var n, r;
            if (!t) return U.Z();
            if ("string" == typeof t) if ("<" == (t = t.trim())[0] && I.test(t)) n = U.fragment(t, RegExp.$1, e), t = null; else {
                if (e !== w) return x(e).find(t);
                n = U.qsa(k, t)
            } else {
                if (a(t)) return x(k).ready(t);
                if (U.isZ(t)) return t;
                if (K(t)) r = t, n = D.call(r, function (t) {
                    return null != t
                }); else if (i(t)) n = [t], t = null; else if (I.test(t)) n = U.fragment(t.trim(), RegExp.$1, e), t = null; else {
                    if (e !== w) return x(e).find(t);
                    n = U.qsa(k, t)
                }
            }
            return U.Z(n, t)
        }, (x = function (t, e) {
            return U.init(t, e)
        }).extend = function (e) {
            var n, t = E.call(arguments, 1);
            return "boolean" == typeof e && (n = e, e = t.shift()), t.forEach(function (t) {
                !function t(e, n, r) {
                    for (b in n) r && (l(n[b]) || K(n[b])) ? (l(n[b]) && !l(e[b]) && (e[b] = {}), K(n[b]) && !K(e[b]) && (e[b] = []), t(e[b], n[b], r)) : n[b] !== w && (e[b] = n[b])
                }(e, t, n)
            }), e
        }, U.qsa = function (t, e) {
            var n, r = "#" == e[0], i = !r && "." == e[0], o = r || i ? e.slice(1) : e, a = z.test(o);
            return t.getElementById && a && r ? (n = t.getElementById(o)) ? [n] : [] : 1 !== t.nodeType && 9 !== t.nodeType && 11 !== t.nodeType ? [] : E.call(a && !r && t.getElementsByClassName ? i ? t.getElementsByClassName(o) : t.getElementsByTagName(e) : t.querySelectorAll(e))
        }, x.contains = k.documentElement.contains ? function (t, e) {
            return t !== e && t.contains(e)
        } : function (t, e) {
            for (; e && (e = e.parentNode);) if (e === t) return !0;
            return !1
        }, x.type = u, x.isFunction = a, x.isWindow = o, x.isArray = K, x.isPlainObject = l, x.isEmptyObject = function (t) {
            var e;
            for (e in t) return !1;
            return !0
        }, x.isNumeric = function (t) {
            var e = Number(t), n = typeof t;
            return null != t && "boolean" != n && ("string" != n || t.length) && !isNaN(e) && isFinite(e) || !1
        }, x.inArray = function (t, e, n) {
            return S.indexOf.call(e, t, n)
        }, x.camelCase = $, x.trim = function (t) {
            return null == t ? "" : String.prototype.trim.call(t)
        }, x.uuid = 0, x.support = {}, x.expr = {}, x.noop = function () {
        }, x.map = function (t, e) {
            var n, r, i, o, a = [];
            if (f(t)) for (r = 0; r < t.length; r++) null != (n = e(t[r], r)) && a.push(n); else for (i in t) null != (n = e(t[i], i)) && a.push(n);
            return 0 < (o = a).length ? x.fn.concat.apply([], o) : o
        }, x.each = function (t, e) {
            var n, r;
            if (f(t)) {
                for (n = 0; n < t.length; n++) if (!1 === e.call(t[n], n, t[n])) return t
            } else for (r in t) if (!1 === e.call(t[r], r, t[r])) return t;
            return t
        }, x.grep = function (t, e) {
            return D.call(t, e)
        }, c.JSON && (x.parseJSON = JSON.parse), x.each("Boolean Number String Function Array Date RegExp Object Error".split(" "), function (t, e) {
            V["[object " + e + "]"] = e.toLowerCase()
        }), x.fn = {
            constructor: U.Z,
            length: 0,
            forEach: S.forEach,
            reduce: S.reduce,
            push: S.push,
            sort: S.sort,
            splice: S.splice,
            indexOf: S.indexOf,
            concat: function () {
                var t, e, n = [];
                for (t = 0; t < arguments.length; t++) e = arguments[t], n[t] = U.isZ(e) ? e.toArray() : e;
                return N.apply(U.isZ(this) ? this.toArray() : this, n)
            },
            map: function (n) {
                return x(x.map(this, function (t, e) {
                    return n.call(t, e, t)
                }))
            },
            slice: function () {
                return x(E.apply(this, arguments))
            },
            ready: function (t) {
                return Z.test(k.readyState) && k.body ? t(x) : k.addEventListener("DOMContentLoaded", function () {
                    t(x)
                }, !1), this
            },
            get: function (t) {
                return t === w ? E.call(this) : this[0 <= t ? t : t + this.length]
            },
            toArray: function () {
                return this.get()
            },
            size: function () {
                return this.length
            },
            remove: function () {
                return this.each(function () {
                    null != this.parentNode && this.parentNode.removeChild(this)
                })
            },
            each: function (n) {
                return S.every.call(this, function (t, e) {
                    return !1 !== n.call(t, e, t)
                }), this
            },
            filter: function (e) {
                return a(e) ? this.not(this.not(e)) : x(D.call(this, function (t) {
                    return U.matches(t, e)
                }))
            },
            add: function (t, e) {
                return x(T(this.concat(x(t, e))))
            },
            is: function (t) {
                return 0 < this.length && U.matches(this[0], t)
            },
            not: function (e) {
                var n = [];
                if (a(e) && e.call !== w) this.each(function (t) {
                    e.call(this, t) || n.push(this)
                }); else {
                    var r = "string" == typeof e ? this.filter(e) : f(e) && a(e.item) ? E.call(e) : x(e);
                    this.forEach(function (t) {
                        r.indexOf(t) < 0 && n.push(t)
                    })
                }
                return x(n)
            },
            has: function (t) {
                return this.filter(function () {
                    return i(t) ? x.contains(this, t) : x(this).find(t).size()
                })
            },
            eq: function (t) {
                return -1 === t ? this.slice(t) : this.slice(t, +t + 1)
            },
            first: function () {
                var t = this[0];
                return t && !i(t) ? t : x(t)
            },
            last: function () {
                var t = this[this.length - 1];
                return t && !i(t) ? t : x(t)
            },
            find: function (t) {
                var n = this;
                return t ? "object" == typeof t ? x(t).filter(function () {
                    var e = this;
                    return S.some.call(n, function (t) {
                        return x.contains(t, e)
                    })
                }) : 1 == this.length ? x(U.qsa(this[0], t)) : this.map(function () {
                    return U.qsa(this, t)
                }) : x()
            },
            closest: function (n, r) {
                var i = [], o = "object" == typeof n && x(n);
                return this.each(function (t, e) {
                    for (; e && !(o ? 0 <= o.indexOf(e) : U.matches(e, n));) e = e !== r && !s(e) && e.parentNode;
                    e && i.indexOf(e) < 0 && i.push(e)
                }), x(i)
            },
            parents: function (t) {
                for (var e = [], n = this; 0 < n.length;) n = x.map(n, function (t) {
                    return (t = t.parentNode) && !s(t) && e.indexOf(t) < 0 ? (e.push(t), t) : void 0
                });
                return v(e, t)
            },
            parent: function (t) {
                return v(T(this.pluck("parentNode")), t)
            },
            children: function (t) {
                return v(this.map(function () {
                    return r(this)
                }), t)
            },
            contents: function () {
                return this.map(function () {
                    return this.contentDocument || E.call(this.childNodes)
                })
            },
            siblings: function (t) {
                return v(this.map(function (t, e) {
                    return D.call(r(e.parentNode), function (t) {
                        return t !== e
                    })
                }), t)
            },
            empty: function () {
                return this.each(function () {
                    this.innerHTML = ""
                })
            },
            pluck: function (e) {
                return x.map(this, function (t) {
                    return t[e]
                })
            },
            show: function () {
                return this.each(function () {
                    var t, e, n;
                    "none" == this.style.display && (this.style.display = ""), "none" == getComputedStyle(this, "").getPropertyValue("display") && (this.style.display = (t = this.nodeName, C[t] || (e = k.createElement(t), k.body.appendChild(e), n = getComputedStyle(e, "").getPropertyValue("display"), e.parentNode.removeChild(e), "none" == n && (n = "block"), C[t] = n), C[t]))
                })
            },
            replaceWith: function (t) {
                return this.before(t).remove()
            },
            wrap: function (e) {
                var n = a(e);
                if (this[0] && !n) var r = x(e).get(0), i = r.parentNode || 1 < this.length;
                return this.each(function (t) {
                    x(this).wrapAll(n ? e.call(this, t) : i ? r.cloneNode(!0) : r)
                })
            },
            wrapAll: function (t) {
                if (this[0]) {
                    x(this[0]).before(t = x(t));
                    for (var e; (e = t.children()).length;) t = e.first();
                    x(t).append(this)
                }
                return this
            },
            wrapInner: function (i) {
                var o = a(i);
                return this.each(function (t) {
                    var e = x(this), n = e.contents(), r = o ? i.call(this, t) : i;
                    n.length ? n.wrapAll(r) : e.append(r)
                })
            },
            unwrap: function () {
                return this.parent().each(function () {
                    x(this).replaceWith(x(this).children())
                }), this
            },
            clone: function () {
                return this.map(function () {
                    return this.cloneNode(!0)
                })
            },
            hide: function () {
                return this.css("display", "none")
            },
            toggle: function (e) {
                return this.each(function () {
                    var t = x(this);
                    (e === w ? "none" == t.css("display") : e) ? t.show() : t.hide()
                })
            },
            prev: function (t) {
                return x(this.pluck("previousElementSibling")).filter(t || "*")
            },
            next: function (t) {
                return x(this.pluck("nextElementSibling")).filter(t || "*")
            },
            html: function (n) {
                return 0 in arguments ? this.each(function (t) {
                    var e = this.innerHTML;
                    x(this).empty().append(m(this, n, t, e))
                }) : 0 in this ? this[0].innerHTML : null
            },
            text: function (n) {
                return 0 in arguments ? this.each(function (t) {
                    var e = m(this, n, t, this.textContent);
                    this.textContent = null == e ? "" : "" + e
                }) : 0 in this ? this.pluck("textContent").join("") : null
            },
            attr: function (e, n) {
                var t;
                return "string" != typeof e || 1 in arguments ? this.each(function (t) {
                    if (1 === this.nodeType) if (i(e)) for (b in e) g(this, b, e[b]); else g(this, e, m(this, n, t, this.getAttribute(e)))
                }) : 0 in this && 1 == this[0].nodeType && null != (t = this[0].getAttribute(e)) ? t : w
            },
            removeAttr: function (t) {
                return this.each(function () {
                    1 === this.nodeType && t.split(" ").forEach(function (t) {
                        g(this, t)
                    }, this)
                })
            },
            prop: function (e, n) {
                return e = J[e] || e, 1 in arguments ? this.each(function (t) {
                    this[e] = m(this, n, t, this[e])
                }) : this[0] && this[0][e]
            },
            removeProp: function (t) {
                return t = J[t] || t, this.each(function () {
                    delete this[t]
                })
            },
            data: function (t, e) {
                var n = "data-" + t.replace(M, "-$1").toLowerCase(),
                    r = 1 in arguments ? this.attr(n, e) : this.attr(n);
                return null !== r ? y(r) : w
            },
            val: function (e) {
                return 0 in arguments ? (null == e && (e = ""), this.each(function (t) {
                    this.value = m(this, e, t, this.value)
                })) : this[0] && (this[0].multiple ? x(this[0]).find("option").filter(function () {
                    return this.selected
                }).pluck("value") : this[0].value)
            },
            offset: function (o) {
                if (o) return this.each(function (t) {
                    var e = x(this), n = m(this, o, t, e.offset()), r = e.offsetParent().offset(),
                        i = {top: n.top - r.top, left: n.left - r.left};
                    "static" == e.css("position") && (i.position = "relative"), e.css(i)
                });
                if (!this.length) return null;
                if (k.documentElement !== this[0] && !x.contains(k.documentElement, this[0])) return {top: 0, left: 0};
                var t = this[0].getBoundingClientRect();
                return {
                    left: t.left + c.pageXOffset,
                    top: t.top + c.pageYOffset,
                    width: Math.round(t.width),
                    height: Math.round(t.height)
                }
            },
            css: function (t, e) {
                if (arguments.length < 2) {
                    var n = this[0];
                    if ("string" == typeof t) {
                        if (!n) return;
                        return n.style[$(t)] || getComputedStyle(n, "").getPropertyValue(t)
                    }
                    if (K(t)) {
                        if (!n) return;
                        var r = {}, i = getComputedStyle(n, "");
                        return x.each(t, function (t, e) {
                            r[e] = n.style[$(e)] || i.getPropertyValue(e)
                        }), r
                    }
                }
                var o = "";
                if ("string" == u(t)) e || 0 === e ? o = h(t) + ":" + p(t, e) : this.each(function () {
                    this.style.removeProperty(h(t))
                }); else for (b in t) t[b] || 0 === t[b] ? o += h(b) + ":" + p(b, t[b]) + ";" : this.each(function () {
                    this.style.removeProperty(h(b))
                });
                return this.each(function () {
                    this.style.cssText += ";" + o
                })
            },
            index: function (t) {
                return t ? this.indexOf(x(t)[0]) : this.parent().children().indexOf(this[0])
            },
            hasClass: function (t) {
                return !!t && S.some.call(this, function (t) {
                    return this.test(j(t))
                }, n(t))
            },
            addClass: function (n) {
                return n ? this.each(function (t) {
                    if ("className" in this) {
                        _ = [];
                        var e = j(this);
                        m(this, n, t, e).split(/\s+/g).forEach(function (t) {
                            x(this).hasClass(t) || _.push(t)
                        }, this), _.length && j(this, e + (e ? " " : "") + _.join(" "))
                    }
                }) : this
            },
            removeClass: function (e) {
                return this.each(function (t) {
                    if ("className" in this) {
                        if (e === w) return j(this, "");
                        _ = j(this), m(this, e, t, _).split(/\s+/g).forEach(function (t) {
                            _ = _.replace(n(t), " ")
                        }), j(this, _.trim())
                    }
                })
            },
            toggleClass: function (n, r) {
                return n ? this.each(function (t) {
                    var e = x(this);
                    m(this, n, t, j(this)).split(/\s+/g).forEach(function (t) {
                        (r === w ? !e.hasClass(t) : r) ? e.addClass(t) : e.removeClass(t)
                    })
                }) : this
            },
            scrollTop: function (t) {
                if (this.length) {
                    var e = "scrollTop" in this[0];
                    return t === w ? e ? this[0].scrollTop : this[0].pageYOffset : this.each(e ? function () {
                        this.scrollTop = t
                    } : function () {
                        this.scrollTo(this.scrollX, t)
                    })
                }
            },
            scrollLeft: function (t) {
                if (this.length) {
                    var e = "scrollLeft" in this[0];
                    return t === w ? e ? this[0].scrollLeft : this[0].pageXOffset : this.each(e ? function () {
                        this.scrollLeft = t
                    } : function () {
                        this.scrollTo(t, this.scrollY)
                    })
                }
            },
            position: function () {
                if (this.length) {
                    var t = this[0], e = this.offsetParent(), n = this.offset(),
                        r = q.test(e[0].nodeName) ? {top: 0, left: 0} : e.offset();
                    return n.top -= parseFloat(x(t).css("margin-top")) || 0, n.left -= parseFloat(x(t).css("margin-left")) || 0, r.top += parseFloat(x(e[0]).css("border-top-width")) || 0, r.left += parseFloat(x(e[0]).css("border-left-width")) || 0, {
                        top: n.top - r.top,
                        left: n.left - r.left
                    }
                }
            },
            offsetParent: function () {
                return this.map(function () {
                    for (var t = this.offsetParent || k.body; t && !q.test(t.nodeName) && "static" == x(t).css("position");) t = t.offsetParent;
                    return t
                })
            }
        }, x.fn.detach = x.fn.remove, ["width", "height"].forEach(function (r) {
            var i = r.replace(/./, function (t) {
                return t[0].toUpperCase()
            });
            x.fn[r] = function (e) {
                var t, n = this[0];
                return e === w ? o(n) ? n["inner" + i] : s(n) ? n.documentElement["scroll" + i] : (t = this.offset()) && t[r] : this.each(function (t) {
                    (n = x(this)).css(r, m(this, e, t, n[r]()))
                })
            }
        }), ["after", "prepend", "before", "append"].forEach(function (e, a) {
            var s = a % 2;
            x.fn[e] = function () {
                var n, r, i = x.map(arguments, function (t) {
                    var e = [];
                    return "array" == (n = u(t)) ? (t.forEach(function (t) {
                        return t.nodeType !== w ? e.push(t) : x.zepto.isZ(t) ? e = e.concat(t.get()) : void (e = e.concat(U.fragment(t)))
                    }), e) : "object" == n || null == t ? t : U.fragment(t)
                }), o = 1 < this.length;
                return i.length < 1 ? this : this.each(function (t, e) {
                    r = s ? e : e.parentNode, e = 0 == a ? e.nextSibling : 1 == a ? e.firstChild : 2 == a ? e : null;
                    var n = x.contains(k.documentElement, r);
                    i.forEach(function (t) {
                        if (o) t = t.cloneNode(!0); else if (!r) return x(t).remove();
                        r.insertBefore(t, e), n && function t(e, n) {
                            n(e);
                            for (var r = 0, i = e.childNodes.length; r < i; r++) t(e.childNodes[r], n)
                        }(t, function (t) {
                            if (!(null == t.nodeName || "SCRIPT" !== t.nodeName.toUpperCase() || t.type && "text/javascript" !== t.type || t.src)) {
                                var e = t.ownerDocument ? t.ownerDocument.defaultView : c;
                                e.eval.call(e, t.innerHTML)
                            }
                        })
                    })
                })
            }, x.fn[s ? e + "To" : "insert" + (a ? "Before" : "After")] = function (t) {
                return x(t)[e](this), this
            }
        }), U.Z.prototype = d.prototype = x.fn, U.uniq = T, U.deserializeValue = y, x.zepto = U, x
    }();
    return c.Zepto = d, void 0 === c.$ && (c.$ = d), function (l) {
        function f(t) {
            return t._zid || (t._zid = e++)
        }

        function a(t, e, n, r) {
            if ((e = h(e)).ns) var i = (o = e.ns, new RegExp("(?:^| )" + o.replace(" ", " .* ?") + "(?: |$)"));
            var o;
            return (x[f(t)] || []).filter(function (t) {
                return t && (!e.e || t.e == e.e) && (!e.ns || i.test(t.ns)) && (!n || f(t.fn) === f(n)) && (!r || t.sel == r)
            })
        }

        function h(t) {
            var e = ("" + t).split(".");
            return {e: e[0], ns: e.slice(1).sort().join(" ")}
        }

        function p(t, e) {
            return t.del && !n && t.e in r || !!e
        }

        function d(t) {
            return _[t] || n && r[t] || t
        }

        function u(i, t, e, o, a, s, c) {
            var n = f(i), u = x[n] || (x[n] = []);
            t.split(/\s/).forEach(function (t) {
                if ("ready" == t) return l(document).ready(e);
                var n = h(t);
                n.fn = e, n.sel = a, n.e in _ && (e = function (t) {
                    var e = t.relatedTarget;
                    return !e || e !== this && !l.contains(this, e) ? n.fn.apply(this, arguments) : void 0
                });
                var r = (n.del = s) || e;
                n.proxy = function (t) {
                    if (!(t = m(t)).isImmediatePropagationStopped()) {
                        t.data = o;
                        var e = r.apply(i, t._args == j ? [t] : [t].concat(t._args));
                        return !1 === e && (t.preventDefault(), t.stopPropagation()), e
                    }
                }, n.i = u.length, u.push(n), "addEventListener" in i && i.addEventListener(d(n.e), n.proxy, p(n, c))
            })
        }

        function v(e, t, n, r, i) {
            var o = f(e);
            (t || "").split(/\s/).forEach(function (t) {
                a(e, t, n, r).forEach(function (t) {
                    delete x[o][t.i], "removeEventListener" in e && e.removeEventListener(d(t.e), t.proxy, p(t, i))
                })
            })
        }

        function m(r, i) {
            return (i || !r.isDefaultPrevented) && (i || (i = r), l.each(t, function (t, e) {
                var n = i[t];
                r[t] = function () {
                    return this[e] = s, n && n.apply(i, arguments)
                }, r[e] = $
            }), r.timeStamp || (r.timeStamp = Date.now()), (i.defaultPrevented !== j ? i.defaultPrevented : "returnValue" in i ? !1 === i.returnValue : i.getPreventDefault && i.getPreventDefault()) && (r.isDefaultPrevented = s)), r
        }

        function g(t) {
            var e, n = {originalEvent: t};
            for (e in t) i.test(e) || t[e] === j || (n[e] = t[e]);
            return m(n, t)
        }

        var j, e = 1, y = Array.prototype.slice, w = l.isFunction, b = function (t) {
                return "string" == typeof t
            }, x = {}, o = {}, n = "onfocusin" in c, r = {focus: "focusin", blur: "focusout"},
            _ = {mouseenter: "mouseover", mouseleave: "mouseout"};
        o.click = o.mousedown = o.mouseup = o.mousemove = "MouseEvents", l.event = {
            add: u,
            remove: v
        }, l.proxy = function (t, e) {
            var n = 2 in arguments && y.call(arguments, 2);
            if (w(t)) {
                var r = function () {
                    return t.apply(e, n ? n.concat(y.call(arguments)) : arguments)
                };
                return r._zid = f(t), r
            }
            if (b(e)) return n ? (n.unshift(t[e], t), l.proxy.apply(null, n)) : l.proxy(t[e], t);
            throw new TypeError("expected function")
        }, l.fn.bind = function (t, e, n) {
            return this.on(t, e, n)
        }, l.fn.unbind = function (t, e) {
            return this.off(t, e)
        }, l.fn.one = function (t, e, n, r) {
            return this.on(t, e, n, r, 1)
        };
        var s = function () {
            return !0
        }, $ = function () {
            return !1
        }, i = /^([A-Z]|returnValue$|layer[XY]$|webkitMovement[XY]$)/, t = {
            preventDefault: "isDefaultPrevented",
            stopImmediatePropagation: "isImmediatePropagationStopped",
            stopPropagation: "isPropagationStopped"
        };
        l.fn.delegate = function (t, e, n) {
            return this.on(e, t, n)
        }, l.fn.undelegate = function (t, e, n) {
            return this.off(e, t, n)
        }, l.fn.live = function (t, e) {
            return l(document.body).delegate(this.selector, t, e), this
        }, l.fn.die = function (t, e) {
            return l(document.body).undelegate(this.selector, t, e), this
        }, l.fn.on = function (e, i, n, o, a) {
            var s, c, r = this;
            return e && !b(e) ? (l.each(e, function (t, e) {
                r.on(t, i, n, e, a)
            }), r) : (b(i) || w(o) || !1 === o || (o = n, n = i, i = j), (o === j || !1 === n) && (o = n, n = j), !1 === o && (o = $), r.each(function (t, r) {
                a && (s = function (t) {
                    return v(r, t.type, o), o.apply(this, arguments)
                }), i && (c = function (t) {
                    var e, n = l(t.target).closest(i, r).get(0);
                    return n && n !== r ? (e = l.extend(g(t), {
                        currentTarget: n,
                        liveFired: r
                    }), (s || o).apply(n, [e].concat(y.call(arguments, 1)))) : void 0
                }), u(r, e, o, n, i, c || s)
            }))
        }, l.fn.off = function (t, n, e) {
            var r = this;
            return t && !b(t) ? (l.each(t, function (t, e) {
                r.off(t, n, e)
            }), r) : (b(n) || w(e) || !1 === e || (e = n, n = j), !1 === e && (e = $), r.each(function () {
                v(this, t, e, n)
            }))
        }, l.fn.trigger = function (t, e) {
            return (t = b(t) || l.isPlainObject(t) ? l.Event(t) : m(t))._args = e, this.each(function () {
                t.type in r && "function" == typeof this[t.type] ? this[t.type]() : "dispatchEvent" in this ? this.dispatchEvent(t) : l(this).triggerHandler(t, e)
            })
        }, l.fn.triggerHandler = function (n, r) {
            var i, o;
            return this.each(function (t, e) {
                (i = g(b(n) ? l.Event(n) : n))._args = r, i.target = e, l.each(a(e, n.type || n), function (t, e) {
                    return o = e.proxy(i), !i.isImmediatePropagationStopped() && void 0
                })
            }), o
        }, "focusin focusout focus blur load resize scroll unload click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select keydown keypress keyup error".split(" ").forEach(function (e) {
            l.fn[e] = function (t) {
                return 0 in arguments ? this.bind(e, t) : this.trigger(e)
            }
        }), l.Event = function (t, e) {
            b(t) || (t = (e = t).type);
            var n = document.createEvent(o[t] || "Events"), r = !0;
            if (e) for (var i in e) "bubbles" == i ? r = !!e[i] : n[i] = e[i];
            return n.initEvent(t, r, !0), m(n)
        }
    }(d), function (Dh) {
        function Fh(t, e, n, r) {
            return t.global ? (i = e || Wh, o = n, a = r, s = Dh.Event(o), Dh(i).trigger(s, a), !s.isDefaultPrevented()) : void 0;
            var i, o, a, s
        }

        function Ih(t, e) {
            var n = e.context;
            return !1 !== e.beforeSend.call(n, t, e) && !1 !== Fh(e, n, "ajaxBeforeSend", [t, e]) && void Fh(e, n, "ajaxSend", [t, e])
        }

        function Jh(t, e, n, r) {
            var i = n.context, o = "success";
            n.success.call(i, t, o, e), r && r.resolveWith(i, [t, o, e]), Fh(n, i, "ajaxSuccess", [e, n, t]), Lh(o, e, n)
        }

        function Kh(t, e, n, r, i) {
            var o = r.context;
            r.error.call(o, n, e, t), i && i.rejectWith(o, [n, e, t]), Fh(r, o, "ajaxError", [n, r, t || e]), Lh(e, n, r)
        }

        function Lh(t, e, n) {
            var r, i = n.context;
            n.complete.call(i, e, t), Fh(n, i, "ajaxComplete", [e, n]), (r = n).global && !--Dh.active && Fh(r, null, "ajaxStop")
        }

        function Nh() {
        }

        function Ph(t, e) {
            return "" == e ? t : (t + "&" + e).replace(/[&?]{1,2}/, "?")
        }

        function Rh(t, e, n, r) {
            return Dh.isFunction(e) && (r = n, n = e, e = void 0), Dh.isFunction(n) || (r = n, n = void 0), {
                url: t,
                data: e,
                success: n,
                dataType: r
            }
        }

        var Th, Uh, Vh = +new Date, Wh = c.document, Xh = /<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi,
            Yh = /^(?:text|application)\/javascript/i, Zh = /^(?:text|application)\/xml/i, $h = "application/json",
            _h = "text/html", ai = /^\s*$/, bi = Wh.createElement("a");
        bi.href = c.location.href, Dh.active = 0, Dh.ajaxJSONP = function (n, r) {
            if (!("type" in n)) return Dh.ajax(n);
            var i, o, t = n.jsonpCallback, a = (Dh.isFunction(t) ? t() : t) || "Zepto" + Vh++,
                s = Wh.createElement("script"), u = c[a], e = function (t) {
                    Dh(s).triggerHandler("error", t || "abort")
                }, l = {abort: e};
            return r && r.promise(l), Dh(s).on("load error", function (t, e) {
                clearTimeout(o), Dh(s).off().remove(), "error" != t.type && i ? Jh(i[0], l, n, r) : Kh(null, e || "error", l, n, r), c[a] = u, i && Dh.isFunction(u) && u(i[0]), u = i = void 0
            }), !1 === Ih(l, n) ? e("abort") : (c[a] = function () {
                i = arguments
            }, s.src = n.url.replace(/\?(.+)=\?/, "?$1=" + a), Wh.head.appendChild(s), 0 < n.timeout && (o = setTimeout(function () {
                e("timeout")
            }, n.timeout))), l
        }, Dh.ajaxSettings = {
            type: "GET",
            beforeSend: Nh,
            success: Nh,
            error: Nh,
            complete: Nh,
            context: null,
            global: !0,
            xhr: function () {
                return new c.XMLHttpRequest
            },
            accepts: {
                script: "text/javascript, application/javascript, application/x-javascript",
                json: $h,
                xml: "application/xml, text/xml",
                html: _h,
                text: "text/plain"
            },
            crossDomain: !1,
            timeout: 0,
            processData: !0,
            cache: !0,
            dataFilter: Nh
        }, Dh.ajax = function (mj) {
            var nj, oj, Ni, li, pj = Dh.extend({}, mj || {}), qj = Dh.Deferred && Dh.Deferred();
            for (Th in Dh.ajaxSettings) void 0 === pj[Th] && (pj[Th] = Dh.ajaxSettings[Th]);
            (li = pj).global && 0 == Dh.active++ && Fh(li, null, "ajaxStart"), pj.crossDomain || ((nj = Wh.createElement("a")).href = pj.url, nj.href = nj.href, pj.crossDomain = bi.protocol + "//" + bi.host != nj.protocol + "//" + nj.host), pj.url || (pj.url = c.location.toString()), -1 < (oj = pj.url.indexOf("#")) && (pj.url = pj.url.slice(0, oj)), (Ni = pj).processData && Ni.data && "string" != Dh.type(Ni.data) && (Ni.data = Dh.param(Ni.data, Ni.traditional)), !Ni.data || Ni.type && "GET" != Ni.type.toUpperCase() && "jsonp" != Ni.dataType || (Ni.url = Ph(Ni.url, Ni.data), Ni.data = void 0);
            var rj = pj.dataType, sj = /\?.+=\?/.test(pj.url);
            if (sj && (rj = "jsonp"), !1 !== pj.cache && (mj && !0 === mj.cache || "script" != rj && "jsonp" != rj) || (pj.url = Ph(pj.url, "_=" + Date.now())), "jsonp" == rj) return sj || (pj.url = Ph(pj.url, pj.jsonp ? pj.jsonp + "=?" : !1 === pj.jsonp ? "" : "callback=?")), Dh.ajaxJSONP(pj, qj);
            var tj, uj = pj.accepts[rj], vj = {}, wj = function (t, e) {
                    vj[t.toLowerCase()] = [t, e]
                }, xj = /^([\w-]+:)\/\//.test(pj.url) ? RegExp.$1 : c.location.protocol, yj = pj.xhr(),
                zj = yj.setRequestHeader;
            if (qj && qj.promise(yj), pj.crossDomain || wj("X-Requested-With", "XMLHttpRequest"), wj("Accept", uj || "*/*"), (uj = pj.mimeType || uj) && (-1 < uj.indexOf(",") && (uj = uj.split(",", 2)[0]), yj.overrideMimeType && yj.overrideMimeType(uj)), (pj.contentType || !1 !== pj.contentType && pj.data && "GET" != pj.type.toUpperCase()) && wj("Content-Type", pj.contentType || "application/x-www-form-urlencoded"), pj.headers) for (Uh in pj.headers) wj(Uh, pj.headers[Uh]);
            if (yj.setRequestHeader = wj, !(yj.onreadystatechange = function () {
                if (4 == yj.readyState) {
                    yj.onreadystatechange = Nh, clearTimeout(tj);
                    var Dj, Ej = !1;
                    if (200 <= yj.status && yj.status < 300 || 304 == yj.status || 0 == yj.status && "file:" == xj) {
                        if (rj = rj || ((Ki = pj.mimeType || yj.getResponseHeader("content-type")) && (Ki = Ki.split(";", 2)[0]), Ki && (Ki == _h ? "html" : Ki == $h ? "json" : Yh.test(Ki) ? "script" : Zh.test(Ki) && "xml") || "text"), "arraybuffer" == yj.responseType || "blob" == yj.responseType) Dj = yj.response; else {
                            Dj = yj.responseText;
                            try {
                                Dj = function (t, e, n) {
                                    if (n.dataFilter == Nh) return t;
                                    var r = n.context;
                                    return n.dataFilter.call(r, t, e)
                                }(Dj, rj, pj), "script" == rj ? eval(Dj) : "xml" == rj ? Dj = yj.responseXML : "json" == rj && (Dj = ai.test(Dj) ? null : Dh.parseJSON(Dj))
                            } catch (t) {
                                Ej = t
                            }
                            if (Ej) return Kh(Ej, "parsererror", yj, pj, qj)
                        }
                        Jh(Dj, yj, pj, qj)
                    } else Kh(yj.statusText || null, yj.status ? "error" : "abort", yj, pj, qj)
                }
                var Ki
            }) === Ih(yj, pj)) return yj.abort(), Kh(null, "abort", yj, pj, qj), yj;
            var Aj = !("async" in pj) || pj.async;
            if (yj.open(pj.type, pj.url, Aj, pj.username, pj.password), pj.xhrFields) for (Uh in pj.xhrFields) yj[Uh] = pj.xhrFields[Uh];
            for (Uh in vj) zj.apply(yj, vj[Uh]);
            return 0 < pj.timeout && (tj = setTimeout(function () {
                yj.onreadystatechange = Nh, yj.abort(), Kh(null, "timeout", yj, pj, qj)
            }, pj.timeout)), yj.send(pj.data ? pj.data : null), yj
        }, Dh.get = function () {
            return Dh.ajax(Rh.apply(null, arguments))
        }, Dh.post = function () {
            var t = Rh.apply(null, arguments);
            return t.type = "POST", Dh.ajax(t)
        }, Dh.getJSON = function () {
            var t = Rh.apply(null, arguments);
            return t.dataType = "json", Dh.ajax(t)
        }, Dh.fn.load = function (t, e, n) {
            if (!this.length) return this;
            var r, i = this, o = t.split(/\s/), a = Rh(t, e, n), s = a.success;
            return 1 < o.length && (a.url = o[0], r = o[1]), a.success = function (t) {
                i.html(r ? Dh("<div>").html(t.replace(Xh, "")).find(r) : t), s && s.apply(i, arguments)
            }, Dh.ajax(a), this
        };
        var ci = encodeURIComponent;
        Dh.param = function (t, e) {
            var n = [];
            return n.add = function (t, e) {
                Dh.isFunction(e) && (e = e()), null == e && (e = ""), this.push(ci(t) + "=" + ci(e))
            }, function n(r, t, i, o) {
                var a, s = Dh.isArray(t), c = Dh.isPlainObject(t);
                Dh.each(t, function (t, e) {
                    a = Dh.type(e), o && (t = i ? o : o + "[" + (c || "object" == a || "array" == a ? t : "") + "]"), !o && s ? r.add(e.name, e.value) : "array" == a || !i && "object" == a ? n(r, e, i, t) : r.add(t, e)
                })
            }(n, t, e), n.join("&").replace(/%20/g, "+")
        }
    }(d), (Wj = d).fn.serializeArray = function () {
        var n, r, e = [], i = function (t) {
            return t.forEach ? t.forEach(i) : void e.push({name: n, value: t})
        };
        return this[0] && Wj.each(this[0].elements, function (t, e) {
            r = e.type, (n = e.name) && "fieldset" != e.nodeName.toLowerCase() && !e.disabled && "submit" != r && "reset" != r && "button" != r && "file" != r && ("radio" != r && "checkbox" != r || e.checked) && i(Wj(e).val())
        }), e
    }, Wj.fn.serialize = function () {
        var e = [];
        return this.serializeArray().forEach(function (t) {
            e.push(encodeURIComponent(t.name) + "=" + encodeURIComponent(t.value))
        }), e.join("&")
    }, Wj.fn.submit = function (t) {
        if (0 in arguments) this.bind("submit", t); else if (this.length) {
            var e = Wj.Event("submit");
            this.eq(0).trigger(e), e.isDefaultPrevented() || this.get(0).submit()
        }
        return this
    }, function () {
        try {
            getComputedStyle(void 0)
        } catch (t) {
            var n = getComputedStyle;
            c.getComputedStyle = function (t, e) {
                try {
                    return n(t, e)
                } catch (t) {
                    return null
                }
            }
        }
    }(), d
});
var __showtime = 0;

function ShowTip(t, e) {
    var n = $("#loading");
    if (0 == n.length) {
        n = $('<div id="loading"><table><tr><td><img id="loadingimage" src="./img/1.png" alt="loading.." /></td><td id="loadingtxt">Loading content, please wait..</td></tr></table></div>'), $("body").append(n)
    }
    $("#loadingtxt").text(t);
    var r = 2e3;
    "ok" == e ? $("#loadingimage").attr("src", "./img/1.png") : "loading" == e ? ($("#loadingimage").attr("src", "./img/2.gif"), r = 1e4) : "w" == e ? $("#loadingimage").attr("src", "/img/4.png") : $("#loadingimage").attr("src", "./res/3.png"), clearTimeout(__showtime), n.show();
    __showtime = setTimeout(function () {
        n.hide()
    }, r)
}

function isValidIpAddress(t) {
    var e = 0, n = 0;
    if ("0.0.0.0" == t || "255.255.255.255" == t) return !1;
    var r = t.split(".");
    if (4 != r.length) return !1;
    for (e = 0; e < 4; e++) {
        if (isNaN(r[e]) || "" == r[e] || "+" == r[e].charAt(0) || "-" == r[e].charAt(0)) return !1;
        if (3 < r[e].length || r[e].length < 1) return !1;
        if (!isInteger(r[e]) || r[e] < 0) return !1;
        if (n = parseInt(r[e]), 0 == e && 0 == n) return !1;
        if (n < 0 || 255 < n) return !1
    }
    return !0
}

function isValidSubnetMask(t) {
    var e = 0, n = 0, r = 0, i = !1;
    if ("0.0.0.0" == t) return !1;
    var o = t.split(".");
    if (4 != o.length) return !1;
    for (e = 0; e < 4; e++) {
        if (1 == isNaN(o[e]) || "" == o[e] || "+" == o[e].charAt(0) || "-" == o[e].charAt(0)) return !1;
        if (!isInteger(o[e]) || o[e] < 0) return !1;
        if ((n = parseInt(o[e])) < 0 || 255 < n) return !1;
        if (1 == i && 0 != n) return !1;
        if ((r = getLeftMostZeroBitPos(n)) < getRightMostOneBitPos(n)) return !1;
        r < 8 && (i = !0)
    }
    return !0
}

function isInteger(t) {
    return !!/^(\+|-)?\d+$/.test(t)
}

function checkIPAddress(t, e, n) {
    if (t == e || e == n || t == n) return ShowTip("地址输入错误！", "w", 2e3), !1;
    var r = new Array, i = new Array, o = new Array;
    r = t.split("."), i = e.split("."), o = n.split(".");
    var a = parseInt(r[0]) & parseInt(i[0]), s = parseInt(r[1]) & parseInt(i[1]), c = parseInt(r[2]) & parseInt(i[2]),
        u = parseInt(r[3]) & parseInt(i[3]), l = parseInt(o[0]) & parseInt(i[0]), f = parseInt(o[1]) & parseInt(i[1]),
        h = parseInt(o[2]) & parseInt(i[2]), p = parseInt(o[3]) & parseInt(i[3]);
    return a == l && s == f && c == h && u == p || (ShowTip("IP地址与子网掩码、默认网关不匹配！", "w", 2e3), !1)
}

/*function mycheckip(t) {
    if (0 == isValidIpAddress(t)) return ShowTip('地址 "' + t + '" 是无效IP地址。', "w", 2e3), !1
}

function checkIP(t, e, n) {
    return 0 == isValidIpAddress(t) ? (ShowTip('地址 "' + t + '" 是无效IP地址。', "w", 2e3), !1) : 0 == isValidSubnetMask(e) ? (ShowTip('子网掩码 "' + e + '" 无效。', "w", 2e3), !1) : 0 == isValidIpAddress(n) ? (ShowTip('地址 "' + n + '" 是无效IP地址。', "w", 2e3), !1) : 0 != checkIPAddress(t, e, n) && void 0
}*/

function getLeftMostZeroBitPos(t) {
    var e = 0, n = [128, 64, 32, 16, 8, 4, 2, 1];
    for (e = 0; e < n.length; e++) if (0 == (t & n[e])) return e;
    return n.length
}

function getRightMostOneBitPos(t) {
    var e = 0, n = [1, 2, 4, 8, 16, 32, 64, 128];
    for (e = 0; e < n.length; e++) if ((t & n[e]) >> e == 1) return n.length - e - 1;
    return -1
}

/*function checkInt(t) {
    var e = new RegExp("^[0-9]*[1-9][0-9]*$");
    if (null == t.match(e)) return ShowTip("请输入正整数!", "w", 2e3), !1
}

function validate(t) {
    return !!/^\d+(?=\.{0,1}\d+$|$)/.test(t)
}

function isPort(t) {
    return !!(/^(\d)+$/g.test(t) && parseInt(t) <= 65535 && 0 <= parseInt(t))
}

function checkNum(t) {
    return !!/^(\d)+$/g.test(t)
}

function toolong(t) {
    return null != t && ("string" != typeof t && (t += ""), 30 <= t.replace(/[^\x00-\xff]/g, "01").length)
}*/

function setCookie(t, e, n) {
    var r = new Date;
    r.setDate(r.getDate() + n), document.cookie = t + "=" + escape(e) + (null == n ? "" : ";expires=" + r.toGMTString())
}

function getCookie(t) {
    return 0 < document.cookie.length && (c_start = document.cookie.indexOf(t + "="), -1 != c_start) ? (c_start = c_start + t.length + 1, c_end = document.cookie.indexOf(";", c_start), -1 == c_end && (c_end = document.cookie.length), unescape(document.cookie.substring(c_start, c_end))) : ""
}

var NextandBefore = 0, NextandBeforeMAX = 0;

function logout() {
    ShowTip("正在注销", "loading", 2e3), window.location.href = "login.html", setCookie("sid", "12345678", 1)
}

function G4_set(t) {
    var e = !1, n = !0;
    "1" == t && (n = !(e = !0)), $("#G41").prop("checked", e), $("#G42").prop("checked", n)
}

function G4_read() {
    return $("#G41").prop("checked") ? "1" : "2"
}

function btnquery() {
    //todo
    u = "/login.do", ShowTip("正在获取数据", "loading", 2e3);
    var t = {opt: "q"};
    t.sid = getCookie("sid"), t = JSON.stringify(t), $.ajax({
        type: "post",
        url: u,
        data: t,
        dataType: "json",
        contentType: "json",
        success: function (t) {
            var e = t.s;
            0 == e ? (ShowTip("获取数据成功", "ok", 2e3), $("#tx_ip").val(t.ip), $("#tx_ipmask").val(t.ipmask), $("#tx_gateway").val(t.gateway), $("#tx_mac").val(t.mac), G4_set(t.g4en), $("#tx_mqtt_addr").val(t.mqttep), $("#tx_mqtt_pass").val(t.mqttpass), $("#tx_des_pass").val(t.despass), $("#tx_productid").val(t.productid), $("#tx_logic").val(t.sn), $("#tx_apn_name").val(t.apnname), $("#tx_apn_user").val(t.apnuser), $("#tx_apn_pass").val(t.apnpass), $("#tx_ver").text(t.ver)) : 2018 == e ? (window.location.href = "login.html", setCookie("sid", "", 1)) : ShowTip(t.c, "w")
        },
        error: function (t) {
            console.log(t), ShowTip("未知错误", "w", 2e3)
        }
    })
}

function btnsave() {
    u = "/login.do", ShowTip("正在保存数据", "loading", 2e3);
    var t = {opt: "s"};
    t.sid = getCookie("sid"), t.ip = $("#tx_ip").val(), t.ipmask = $("#tx_ipmask").val(), t.gateway = $("#tx_gateway").val(), t.mac = $("#tx_mac").val(), t.g4en = G4_read(), t.mqttep = $("#tx_mqtt_addr").val(), t.mqttpass = $("#tx_mqtt_pass").val(), t.despass = $("#tx_des_pass").val(), t.productid = $("#tx_productid").val(), t.apnname = $("#tx_apn_name").val(), t.apnuser = $("#tx_apn_user").val(), t.apnpass = $("#tx_apn_pass").val(), t.sn = $("#tx_logic").val(), t = JSON.stringify(t), $.ajax({
        type: "post",
        url: u,
        data: t,
        dataType: "json",
        contentType: "json",
        success: function (t) {
            var e = t.s;
            0 == e ? ShowTip("保存数据成功", "ok", 2e3) : 2018 == e ? (window.location.href = "login.html", setCookie("sid", "", 1)) : ShowTip(t.c, "w")
        },
        error: function (t) {
            console.log(t), ShowTip("未知错误", "w", 2e3)
        }
    })
}

function showMain(t) {
    ShowTip("获取中", "loading", 5e3), $("#main>.main").hide(), $("#c" + t).show()
}

/*function ajaxcall(t, e, n, r) {
    showMain(t), ShowTip("正在获取数据", "ok", 2e3), $.ajax({
        type: "get",
        url: "/login.do",
        success: r,
        error: function (t) {
            console.log(t)
        }
    })
}*/

function btnreboot() {
    u = "//login.do", ShowTip("正在提交命令", "loading", 2e3);
    var t = {opt: "reboot"};
    t.sid = getCookie("sid"), t = JSON.stringify(t), $.ajax({
        type: "post",
        url: u,
        data: t,
        dataType: "json",
        contentType: "json",
        success: function (t) {
            var e = t.s;
            0 == e ? ShowTip("命令成功下发,请稍后", "ok", 2e3) : 2018 == e ? (window.location.href = "login.html", setCookie("sid", "", 1)) : ShowTip(t.c, "w")
        },
        error: function (t) {
            console.log(t), ShowTip("未知错误", "w", 2e3)
        }
    })
}

/*function ajaxsave(t, e, n) {
    ShowTip("正在保存数据", "ok", 2e3), $.ajax({
        type: "post",
        url: "/login.do",
        data: e,
        dataType: "json",
        success: n
    })
}

function netinfo(t, e) {
    ShowTip("获取中", "loading", 5e3);
    ajaxcall(t, e, {}, function (t) {
        ShowTip(t.msg, "ok", 2e3), $("#IPAddress").val(t.webserver_ip), $("#SubMask").val(t.webserver_netmask), $("#Gateway").val(t.webserver_gateway), $("#MAC").val(t.webserver_mac), $("#netmanip").val(t.webserver_netmanagerip), $("#netserverport").val(t.webserver_sendport)
    })
}

function basicpara(t, e) {
    ShowTip("获取中", "loading", 5e3);
    ajaxcall(t, e, {}, function (t) {
        ShowTip(t.msg, "ok", 2e3), $("#currentSN").val(t.webserver_sn), $("#currentarea").val(t.webserver_logic), $("#hw_version").val(t.hw_version), $("#sf_version").val(t.sf_version)
    })
}

function serverinfor(t, e) {
    ShowTip("获取中", "loading", 5e3);
    ajaxcall(t, e, {}, function (t) {
        0 == t.state ? (ShowTip(t.msg, "ok", 2e3), $("#ServerAddr").val(t.ip), $("#ServerPort").val(t.port)) : ShowTip(t.msg, "w", 2e3)
    })
}

function systemPara(t, e) {
    ShowTip("获取中", "loading", 5e3);
    ajaxcall(t, e, {}, function (t) {
        ShowTip(t.msg, "ok", 2e3), $("#NEName").val("Betelinfo-yz"), $("#SystemOid").val(""), $("#HoldTime").val("1:00"), $("#Descr").val("Betelinfo"), $("#Administrator").val("Administrator"), $("#Location").val("nanjing")
    })
}

function digpara(t, e) {
    ShowTip("获取中", "loading", 5e3);
    ajaxcall(t, e, {}, function (t) {
        console.log(JSON.stringify(t)), ShowTip(t.msg, "ok", 2e3), $("#fmfreq").val(t.webserver_fm_fre), $("#webserver_dvbc_fre").val(t.webserver_dvbc_fre), $("#webserver_symbol").val(t.webserver_symbol), $("#webserver_qam").val(t.webserver_qam), $("#webserver_dtmb_fre").val(t.webserver_dtmb_fre), $("#webserver_dtmb_qam").val(t.webserver_dtmb_qam), $("#PID").val("01"), $("#TableID").val("01")
    })
}*/

/*
function formatstr(t) {
    if (null != t) return t.replace(/"/g, "").replace(/,/g, "")
}

function btnSave(t) {
    ajaxsave(void 0, "webserver_logic:" + $("#currentarea").val() + ",webserver_netmanagerip:" + $("#netmanip").val() + ",webserver_sendport:" + $("#netserverport").val() + ",webserver_ip:" + $("#IPAddress").val() + ",webserver_netmask:" + $("#SubMask").val() + ",webserver_gateway:" + $("#Gateway").val() + ",webserver_dvbc_fre:" + $("#webserver_dvbc_fre").val() + ",webserver_dtmb_fre:" + $("#webserver_dtmb_fre").val() + ",webserver_fm_fre:" + $("#fmfreq").val(), function (t) {
        0 == t.state ? ShowTip(t.msg, "ok", 2e3) : ShowTip(t.msg, "w", 2e3)
    })
}
*/

function btnlogin() {
    u = "/login.do", ShowTip("正在获取数据", "ok", 2e3);
    var t = {};
    t.u = $("#Username").val(), t.p = $("#Password").val(), t.opt = "login", t.opt = "login", t.sid = getCookie("sid"), t = JSON.stringify(t), $.ajax({
        type: "post",
        url: u,
        data: t,
        dataType: "json",
        contentType: "json",
        success: function (t) {
            0 == t.s ? (window.location.href = "/config.html", setCookie("sid", t.sid, 1e3)) : ShowTip(t.c, "w")
        },
        error: function (t) {
            console.log(t)
        }
    })
}

function keyLogin() {
    13 == event.keyCode && btnlogin()
}

function RefreshPage() {
    location.href = document.location.href
}

/*
function phonemenu() {
    var t = $("#bs-example-navbar-collapse-1");
    t.hasClass("in") ? t.removeClass("in") : t.addClass("in")
}*/
