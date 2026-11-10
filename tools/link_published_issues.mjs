/** Link verified GitHub publication records; preserve all execution outcomes. */
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const sub=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../submission');
const pub=JSON.parse(await fs.readFile(`${sub}/evidence/gui/github_published_issues.json`,'utf8'));
const byId=new Map(pub.issues.flatMap(issue=>issue.relatedChecklistIds.map(id=>[id,issue])));
if(pub.issues.length!==29||byId.size!==31)throw new Error('Publication mapping incomplete');
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(`${sub}/GUI_Checklist.xlsx`));
const cl=wb.worksheets.getItem('Checklist'),ex=wb.worksheets.getItem('Execution'),sum=wb.worksheets.getItem('Summary');
const before=JSON.stringify([cl.getRange('A7:M74').values,ex.getRange('A7:J74').values,ex.getRange('M7:M74').values,ex.getRange('A75:M77').values,wb.worksheets.getItem('AI Review').getRange('A1:G74').values]);
let linked=0;
for(let row=7;row<=74;row++){
 const id=cl.getRange(`A${row}`).values[0][0],status=cl.getRange(`M${row}`).values[0][0],issue=byId.get(id);
 if(status==='Failed'){
  if(!issue)throw new Error('No published issue for '+id);
  ex.getRange(`K${row}:L${row}`).values=[[issue.draftId,issue.url]];
  let note=cl.getRange(`N${row}`).values[0][0]??'';
  note=note.replace(/\nGitHub Issue: .*$/,'');
  cl.getRange(`N${row}`).values=[[note+'\nGitHub Issue: '+issue.url]];
  cl.getRange(`A${row}:N${row}`).format.rowHeight=220;linked++;
 }else if(issue)throw new Error('Issue mapped to non-Failed item '+id);
}
if(linked!==31)throw new Error('Expected 31 linked failures');
if(JSON.stringify([cl.getRange('A7:M74').values,ex.getRange('A7:J74').values,ex.getRange('M7:M74').values,ex.getRange('A75:M77').values,wb.worksheets.getItem('AI Review').getRange('A1:G74').values])!==before)throw new Error('Unrelated values changed');
sum.getRange('A22').values=[['29 GitHub Issues link 31 Failed items; evidence pinned to commit 19cbfb0.']];
wb.recalculate();
if(JSON.stringify(sum.getRange('B11:H11').values[0])!==JSON.stringify([65,34,31,0,0,0,0]))throw new Error('Result totals changed');
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:10},maxChars:500})).ndjson);
await fs.mkdir('/tmp/hw03-issue-links',{recursive:true});
for(const[sheetName,range,name]of [['Summary','A1:H22','summary'],['Execution','K7:L11','links'],['Checklist','M65:N66','notes']]){
 const blob=await wb.render({sheetName,range,scale:1,format:'png'});await fs.writeFile(`/tmp/hw03-issue-links/${name}.png`,new Uint8Array(await blob.arrayBuffer()));
}
await(await SpreadsheetFile.exportXlsx(wb)).save(`${sub}/GUI_Checklist.xlsx`);
console.log('Linked 29 verified Issues to 31 Failed rows; all outcomes preserved.');
