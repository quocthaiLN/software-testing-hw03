/** Integrate student-supplied manual observations without inventing run times. */
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const sub=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../submission');
const data=JSON.parse(await fs.readFile(`${sub}/evidence/gui/mobile_execution.json`,'utf8'));
if(data.latest.length!==16)throw new Error('Expected 16 mapped original criteria');
const revisions=JSON.parse(await fs.readFile(`${sub}/mobile_case_revisions.json`,'utf8')).items;
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(`${sub}/GUI_Checklist.xlsx`));
const cl=wb.worksheets.getItem('Checklist'),ex=wb.worksheets.getItem('Execution'),sum=wb.worksheets.getItem('Summary');
const preserved=JSON.stringify([cl.getRange('A7:E74').values,cl.getRange('M7:N58').values,ex.getRange('A7:M58').values,ex.getRange('A75:M77').values,wb.worksheets.getItem('AI Review').getRange('A1:G58').values]);
for(const r of data.latest){
 const row=58+Number(r.itemId.slice(-3));
 if(cl.getRange(`A${row}`).values[0][0]!==r.itemId)throw new Error('ID mismatch');
 const revision=revisions.find(x=>x.id===r.itemId);
 if(revision){
  cl.getRange(`F${row}:I${row}`).values=[[revision.title,revision.steps,revision.expected,revision.source]];
  const review=wb.worksheets.getItem('AI Review');
  review.getRange(`B${row}:E${row}`).values=[['Revise',revision.reason,revision.steps+' Kỳ vọng: '+revision.expected,'Không phải student addition']];
 }
 cl.getRange(`M${row}:N${row}`).values=[[r.status,r.actual]];
 cl.getRange(`M${row}:N${row}`).format.rowHeight=180;
 ex.getRange(`A${row}:M${row}`).values=[[r.runId,r.itemId,revision?'Revision 2 - phone fixture 1912345678; not executed':'Student manual; detailed inputs and provenance in mobile_execution.json','Not supplied - screenshot HH:MM only',data.platform,'Student login: test@eshop.com; original screenshots supplied in chat',r.actual,r.status,r.notes,r.screenshots.join('\n'),'','','Manual run revision not supplied']];
 ex.getRange(`A${row}:M${row}`).format.rowHeight=190;
}
if(JSON.stringify([cl.getRange('A7:E74').values,cl.getRange('M7:N58').values,ex.getRange('A7:M58').values,ex.getRange('A75:M77').values,wb.worksheets.getItem('AI Review').getRange('A1:G58').values])!==preserved)throw new Error('Unrelated content changed');
sum.getRange('A4').values=[['Web execution + student Mobile records; pending criteria identified']];
sum.getRange('D15').values=[['Items concluded P/F']];
sum.getRange('D16').values=[['P/F log rows (not runs)']];
sum.getRange('A21').values=[['Mobile: 8 grouped manual cases; 16 original criteria mapped separately.']];
sum.getRange('A22').values=[['Web: 55 scenario runs. Mobile: 12 uploads; no timestamped run count.']];
cl.getRange('F4').values=[['User Keep; Web + manual Mobile; pending acceptance retained.']];
wb.recalculate();
const metrics=sum.getRange('B11:H11').values[0];
if(JSON.stringify(metrics)!==JSON.stringify([68,33,31,0,1,0,3]))throw new Error(JSON.stringify(metrics));
console.log('Totals [designed, passed, failed, blocked, spec-gap, in-progress, not-run]:',JSON.stringify(metrics));
console.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:10},maxChars:1000})).ndjson);
await fs.mkdir('/tmp/hw03-mobile-review',{recursive:true});
for(const[sheetName,range,filename]of [['Summary','A1:H22','summary'],['Checklist','L59:N62','criteria-top'],['Checklist','L70:N74','criteria-bottom'],['Execution','G65:J66','actual'],['Checklist','F64:I64','revised-name'],['Checklist','F67:I67','revised-address'],['Checklist','F74:I74','revised-network']]){
 const blob=await wb.render({sheetName,range,scale:1,format:'png'});await fs.writeFile(`/tmp/hw03-mobile-review/${filename}.png`,new Uint8Array(await blob.arrayBuffer()));
}
await(await SpreadsheetFile.exportXlsx(wb)).save(`${sub}/GUI_Checklist.xlsx`);
