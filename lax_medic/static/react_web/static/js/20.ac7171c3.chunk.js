(this.webpackJsonplax_medic=this.webpackJsonplax_medic||[]).push([[20],{166:function(e,a,t){e.exports=t.p+"static/media/login1.d7d51fa1.jpg"},88:function(e,a,t){"use strict";t.r(a),t.d(a,"default",(function(){return Q}));var n,o=t(98),r=t(101),c=t(11),s=t(39),l=t(0),i=t.n(l),m=t(397),u=t(351),p=t(80),d=t(398),g=t(257),f=t(301),h=t(339),b=t(341),w=t(300),v=t(167),E=t(338),k=t(36),S=t(350),y=t(349),x=t(255),j=t.n(x),O=t(256),I=t.n(O),C=t(254),P=t.n(C),N=t(148),_=t.n(N),z=t(198),T=t.n(z),W=t(60),D=t(340),F=t(30),J=t(2),A=t(232),R=t.n(A),q=t(234),L=t(235),U=t.n(L);n="localhost"===window.location.hostname||"127.0.0.1"===window.location.hostname?"http://".concat(window.location.hostname,":8000/api/"):"https://auroracomputing.herokuapp.com/api/";var M=U.a.create({baseURL:n,timeout:5e3,headers:{Authorization:localStorage.getItem("access_token")?"JWT "+localStorage.getItem("access_token"):null,"Content-Type":"application/json",accept:"application/json"}});M.interceptors.response.use((function(e){return e}),function(){var e=Object(q.a)(R.a.mark((function e(a){var t,o,r,c;return R.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(t=a.config,"undefined"!==typeof a.response){e.next=4;break}return alert("A server/network error occurred. Looks like CORS might be the problem. Sorry about this - we will get it fixed shortly."),e.abrupt("return",Promise.reject(a));case 4:if(401!==a.response.status||t.url!==n+"token/refresh/"){e.next=7;break}return window.location.href="/login/",e.abrupt("return",Promise.reject(a));case 7:return"token_not_valid"===a.response.data.code&&401===a.response.status&&"Unauthorized"===a.response.statusText&&((o=localStorage.getItem("refresh_token"))?(r=JSON.parse(atob(o.split(".")[1])),c=Math.ceil(Date.now()/1e3),console.log(r.exp),r.exp>c?console.log("--- refresh ---"):(console.log("Refresh token is expired",r.exp,c),localStorage.removeItem("access_token"),localStorage.removeItem("refresh_token"),M.defaults.headers.Authorization=null,window.location.href="/")):(console.log("Refresh token not available."),window.location.href="/login/")),e.abrupt("return",Promise.reject(a));case 9:case"end":return e.stop()}}),e)})));return function(a){return e.apply(this,arguments)}}());var V=M,B=t(166),Y=t.n(B),G=t(43);function H(){return i.a.createElement(E.a,{variant:"body2",color:"textSecondary",align:"center"},"Copyright \xa9 ",i.a.createElement(h.a,{color:"inherit",href:""},"Akelax technologie")," ",(new Date).getFullYear(),".")}var K=Object(k.a)((function(e){return{root:{height:"100vh"},image:{backgroundImage:"url(".concat(Y.a,")"),backgroundRepeat:"no-repeat",backgroundColor:"light"===e.palette.type?e.palette.grey[50]:e.palette.grey[900],backgroundSize:"cover",backgroundPosition:"center"},container:{display:"flex",flexDirection:"column",alignItems:"center"},paper:{margin:e.spacing(8,4),display:"flex",flexDirection:"column",alignItems:"center",maxWidth:450},avatar:{margin:e.spacing(1),backgroundColor:D.a[400]},avatarSuccess:{margin:e.spacing(1),backgroundColor:F.a[400]},avatarWarning:{margin:e.spacing(1),backgroundColor:e.palette.secondary.main},form:{width:"100%",marginTop:e.spacing(2)},submit:{margin:e.spacing(3,0,2)},wrapper:{margin:e.spacing(1),position:"relative"},buttonSuccess:{backgroundColor:F.a[500],"&:hover":{backgroundColor:F.a[700]}},fabProgress:{color:F.a[500],position:"absolute",top:-6,left:-6,zIndex:1},buttonProgress:{color:F.a[500],position:"absolute",top:"50%",left:"50%",marginTop:-12,marginLeft:-12}}}));function Q(e){var a=e.webSocket,t=(Object(s.a)(e,["webSocket"]),K()),n=Object(J.g)(),k=Object(J.h)(),x=Object(G.b)(),O=i.a.useState(!1),C=Object(c.a)(O,2),N=C[0],z=C[1],D=i.a.useState("Identifiez-vous"),F=Object(c.a)(D,2),A=F[0],R=F[1],q=i.a.useState(!0),L=Object(c.a)(q,2),U=L[0],M=L[1],B=Object.freeze({username:"",password:""}),Y=i.a.useState({amount:"",password:"",weight:"",weightRange:"",showPassword:!1}),Q=Object(c.a)(Y,2),X=Q[0],Z=Q[1],$=Object(l.useState)(B),ee=Object(c.a)($,2),ae=ee[0],te=ee[1],ne=function(e){te(Object(r.a)(Object(r.a)({},ae),{},Object(o.a)({},e.target.name,e.target.value.trim())))},oe=function(){setTimeout((function(){a.send(JSON.stringify({type:"login",content:ae}))}),100),a.onmessage=function(e){var a=JSON.parse(e.data);console.log(a),"login"===a.type&&(console.log(a.content),"success"===a.status?(console.log("welcome"),R(a.status),re(a.content.user)):"not allowed"===a.status?(R(a.status),z(!1)):(R(a.status),console.log("vous are not connect"),z(!1)))}},re=function(e){var a=(k.state||{from:{pathname:"/lax_medic"}}).from;x.signin((function(){return setTimeout((function(){n.replace(a)}),1e3),e})),U&&(localStorage.setItem("azerty",ae.username),localStorage.setItem("querty",ae.password))};return i.a.createElement("div",null,i.a.createElement(v.a,{container:!0,component:"main",className:t.root},i.a.createElement(p.a,null),i.a.createElement(v.a,{item:!0,xs:!1,sm:4,md:7,className:t.image}),i.a.createElement(v.a,{item:!0,xs:12,sm:8,md:5,component:b.a,elevation:6,square:!0},i.a.createElement("div",{className:t.container},i.a.createElement("div",{className:t.paper},"Identifiez-vous"===A?i.a.createElement(i.a.Fragment,null,i.a.createElement(m.a,{className:t.avatar},i.a.createElement(T.a,null)),i.a.createElement(E.a,{component:"p",variant:"h5"},A)):"success"===A?i.a.createElement(i.a.Fragment,null,i.a.createElement(m.a,{className:t.avatarSuccess},i.a.createElement(_.a,null)),i.a.createElement(E.a,{component:"p",variant:"h5"},"Bienvenu(e) !!!")):"not allowed"===A?i.a.createElement(i.a.Fragment,null,i.a.createElement(m.a,{className:t.avatarWarning},i.a.createElement(P.a,null)),i.a.createElement(E.a,{component:"p",variant:"h5"},"Vous \xeates pas permi d'entrer")):i.a.createElement(i.a.Fragment,null,i.a.createElement(m.a,{className:t.avatarWarning},i.a.createElement(P.a,null)),i.a.createElement(E.a,{component:"p",variant:"h5"},"Identifiant incorrect")),i.a.createElement("form",{className:t.form,method:"POST",action:".",onSubmit:function(e){e.preventDefault(),N||z(!0),V.post("/token/",{username:ae.username,password:ae.password}).then((function(e){console.log("success"),localStorage.setItem("access_token",e.data.access),localStorage.setItem("refresh_token",e.data.refresh),V.defaults.headers.Authorization="JWT "+localStorage.getItem("access_token"),oe()})).catch((function(e){oe()}))}},i.a.createElement(d.a,{variant:"outlined",margin:"normal",required:!0,fullWidth:!0,id:"username",label:"Votre nom",name:"username",autoComplete:"username",autoFocus:!0,onChange:ne}),i.a.createElement(d.a,{variant:"outlined",margin:"normal",required:!0,fullWidth:!0,name:"password",label:"Password",type:X.showPassword?"text":"password",id:"password",autoComplete:"current-password",onChange:ne,InputProps:{endAdornment:i.a.createElement(y.a,{position:"end"},i.a.createElement(S.a,{"aria-label":"toggle password visibility",onClick:function(){Z(Object(r.a)(Object(r.a)({},X),{},{showPassword:!X.showPassword}))},onMouseDown:function(e){e.preventDefault()},edge:"end"},X.showPassword?i.a.createElement(j.a,null):i.a.createElement(I.a,null)))}}),i.a.createElement(g.a,{control:i.a.createElement(f.a,{checked:U,onChange:function(){return M((function(e){return!e}))},color:"primary",name:"remember"}),label:"se rappeler de moi"}),i.a.createElement(u.a,{type:"submit",fullWidth:!0,variant:"contained",color:"primary",disabled:N,className:t.submit},N&&i.a.createElement(W.a,{size:24,className:t.buttonProgress}),"Se connecter"),i.a.createElement(v.a,{container:!0},i.a.createElement(v.a,{item:!0,xs:!0},i.a.createElement(h.a,{href:"#",variant:"body2"},"Forgot password?")),i.a.createElement(v.a,{item:!0},i.a.createElement(h.a,{href:"#",variant:"body2"},"Don't have an account? Sign Up"))),i.a.createElement(w.a,{mt:5},i.a.createElement(H,null))))))))}}}]);
//# sourceMappingURL=20.ac7171c3.chunk.js.map