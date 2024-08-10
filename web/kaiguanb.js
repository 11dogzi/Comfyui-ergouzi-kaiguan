import{app}from"/scripts/app.js";import{ComfyWidgets}from"/scripts/widgets.js";function generateGroupId(e){return e.title}function renameDuplicateGroups(e){let o=new Set,p={};e.forEach(e=>{var t=e.title;if(o.has(t)){for(;o.has(""+t+p[t]);)p[t]+=1;e.title=""+t+p[t],o.add(e.title)}else o.add(t),p[t]=1})}function showSwitchSettings(n){let e=document.createElement("div");e.style.position="fixed",e.style.top="50%",e.style.left="50%",e.style.transform="translate(-50%, -50%)",e.style.padding="20px",e.style.backgroundColor="#333",e.style.color="#fff",e.style.border="1px solid #ccc",e.style.zIndex=1e3,e.style.maxHeight="80%",e.style.overflowY="auto",e.style.width="400px";var t=document.createElement("h3");t.textContent="2🐕开关设置【set up】",e.appendChild(t),(t=document.createElement("label")).textContent="开关名称【Switch name】: ",e.appendChild(t);let o=document.createElement("input");o.type="text",o.value=n.properties.switchName||"smooth_edge_switch",o.addEventListener("input",()=>{var e=o.value;n.properties.switchName=e,updateSwitchWidgetName(n,e)}),e.appendChild(o);var a=document.createElement("table"),p=(a.style.width="100%",a.style.borderCollapse="collapse",a.style.color="#fff",(t=document.createElement("tr")).innerHTML="<th style='text-align: left;'>组Group</th><th>忽略Bypass</th><th>禁用Disable</th>",t.style.borderBottom="1px solid #ccc",a.appendChild(t),app.graph._groups||[]),p=(void 0===n.properties.bypassGroups&&(n.properties.bypassGroups=[]),void 0===n.properties.disableGroups&&(n.properties.disableGroups=[]),0===p.length?((t=document.createElement("tr")).innerHTML="<td colspan='3' style='text-align: center; padding: 10px;'>没有找到组No group found</td>",a.appendChild(t)):(renameDuplicateGroups(p),p.forEach(e=>{let t=generateGroupId(e),o=document.createElement("tr");var p=document.createElement("input"),e=(p.type="hidden",p.value=t,o.appendChild(p),(p=document.createElement("td")).textContent=e.title,o.appendChild(p),document.createElement("td"));let s=document.createElement("input"),r=(s.type="checkbox",s.checked=n.properties.bypassGroups.includes(t),s.addEventListener("change",()=>{s.checked?(n.properties.bypassGroups.push(t),n.properties.disableGroups=n.properties.disableGroups.filter(e=>e!==t),o.querySelectorAll("input[type='checkbox']").forEach(e=>{e!==s&&(e.checked=!1)})):n.properties.bypassGroups=n.properties.bypassGroups.filter(e=>e!==t),handleGroupControl(n)}),e.appendChild(s),o.appendChild(e),document.createElement("td")),i=document.createElement("input");i.type="checkbox",i.checked=n.properties.disableGroups.includes(t),i.addEventListener("change",()=>{i.checked?(n.properties.disableGroups.push(t),n.properties.bypassGroups=n.properties.bypassGroups.filter(e=>e!==t),o.querySelectorAll("input[type='checkbox']").forEach(e=>{e!==i&&(e.checked=!1)})):n.properties.disableGroups=n.properties.disableGroups.filter(e=>e!==t),handleGroupControl(n)}),r.appendChild(i),o.appendChild(r),o.style.borderBottom="1px solid #ccc",a.appendChild(o)})),e.appendChild(a),(t=document.createElement("button")).textContent="关闭【close】",t.style.marginTop="10px",t.addEventListener("click",()=>{document.body.removeChild(e),handleGroupControl(n)}),e.appendChild(t),document.createElement("button"));p.textContent="灵仙儿和二狗子",p.style.position="absolute",p.style.top="10px",p.style.right="10px",p.style.backgroundColor="#ff69b4",p.style.color="#fff",p.style.border="none",p.style.padding="5px 10px",p.style.borderRadius="5px",p.style.cursor="pointer",p.addEventListener("click",()=>{window.open("https://space.bilibili.com/19723588?spm_id_from=333.1350.jump_directly","_blank")}),e.appendChild(p),document.body.appendChild(e)}function updateSwitchWidgetName(e,t){(e=e.widgets.find(e=>"switchNameWidget"===e.name))&&(e.label=t,app.graph.setDirtyCanvas(!0,!0))}function setGlobalNode(t){app.graph._nodes.forEach(e=>{"GroupSwitchNodeeee"===e.type&&e!==t&&(e.properties.smooth_edge_switch=!1,updateNodeWidgets(e),handleGroupControl(e))})}function updateNodeWidgets(e){(e=e.widgets.find(e=>"switchNameWidget"===e.name))&&(e.value=!1)}function handleGroupControl(e){let o=e.properties.smooth_edge_switch,p=e.properties.bypassGroups,s=e.properties.disableGroups;(app.graph._groups||[]).forEach(e=>{let t=generateGroupId(e);e._nodes.some(e=>e&&["hulue","jinyong","ALLty"].includes(e.type))||(e.recomputeInsideNodes(),e._nodes.forEach(e=>{e&&(e.mode=o?p.includes(t)?4:s.includes(t)?LiteGraph.NEVER:LiteGraph.ALWAYS:LiteGraph.ALWAYS)}))}),app.graph.setDirtyCanvas(!0,!0)}function ensureSwitchNameConsistency(e){var t;"GroupSwitchNodeeee"===e.type&&(t=e.properties.switchName,e=e.widgets.find(e=>"switchNameWidget"===e.name))&&t!==e.label&&(e.label=t,app.graph.setDirtyCanvas(!0,!0))}let originalGetNodeMenuOptions=LGraphCanvas.prototype.getNodeMenuOptions;LGraphCanvas.prototype.getNodeMenuOptions=function(e){var t=originalGetNodeMenuOptions.apply(this,arguments);return"GroupSwitchNodeeee"===e.type&&t.push({content:"2🐕开关设置【set up】",callback:()=>showSwitchSettings(e)}),t},app.registerExtension({name:"Comfy.GroupSwitchNodeeee",async beforeRegisterNodeDef(e,t,o){"GroupSwitchNodeeee"===t.name&&(e.prototype.onNodeCreated=function(){var e;this._initialized||(this._initialized=!0,this.properties={switchName:"smooth_edge_switch",smooth_edge_switch:!1,bypassGroups:[],disableGroups:[]},(e=ComfyWidgets.BOOLEAN(this,"switchNameWidget",{default:!1,label_on:"True",label_off:"False"})).widget.callback=e=>{this.properties.smooth_edge_switch=e,setGlobalNode(this),handleGroupControl(this)},this.widgets=[e.widget])},e.prototype.onSerialize=function(e){e.properties=this.properties},e.prototype.onConfigure=function(e){this.properties=e.properties||{switchName:"smooth_edge_switch",smooth_edge_switch:!1,bypassGroups:[],disableGroups:[]},ensureSwitchNameConsistency(this),handleGroupControl(this)})}}),renameDuplicateGroups(app.graph._groups);