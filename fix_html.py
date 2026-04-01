import re

with open('projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update <style> CSS rules
css_updates = [
    (r'\.sidebar \{\s*width: 220px;\s*min-height: 100vh;\s*background: #fff;\s*border-right: 1px solid #e8edf5;\s*position: fixed;\s*top: 0;\s*left: 0;\s*display: flex;\s*flex-direction: column;\s*padding: 28px 0;\s*z-index: 100;\s*\}', 
     '.sidebar { width: 280px; min-height: 100vh; background: #fff; border-right: 1px solid #e8edf5; position: fixed; top: 0; left: 0; display: flex; flex-direction: column; padding: 40px 0; z-index: 100; }'),
    (r'\.sidebar-logo \{\s*padding: 0 20px 28px 20px;', 
     '.sidebar-logo { padding: 0 40px 40px 40px;'),
    (r'\.sidebar-section \{\s*padding: 20px 12px 0 12px;\s*display: flex;\s*flex-direction: column;\s*gap: 4px;', 
     '.sidebar-section { padding: 32px 24px 0 24px; display: flex; flex-direction: column; gap: 8px;'),
    (r'\.sidebar-bottom \{\s*margin-top: auto;\s*padding: 0 12px;\s*display: flex;\s*flex-direction: column;\s*gap: 4px;', 
     '.sidebar-bottom { margin-top: auto; padding: 0 24px; display: flex; flex-direction: column; gap: 8px;'),
    (r'\.sidebar-item \{\s*display: flex;\s*align-items: center;\s*gap: 12px;\s*padding: 10px 12px;\s*border-radius: 10px;\s*font-size: 14px;', 
     '.sidebar-item { display: flex; align-items: center; gap: 16px; padding: 14px 20px; border-radius: 12px; font-size: 16px;'),
    (r'\.sidebar-divider \{\s*height: 1px;\s*background: #e8edf5;\s*margin: 16px 12px;\s*\}', 
     '.sidebar-divider { height: 1px; background: #e8edf5; margin: 32px 24px; }'),
    (r'\.sidebar-item svg \{\s*width: 18px;\s*height: 18px;\s*flex-shrink: 0;\s*\}', 
     '.sidebar-item svg { width: 24px; height: 24px; flex-shrink: 0; }'),
    (r'\.main-content \{\s*margin-left: 220px;\s*padding: 36px 40px 40px 40px;\s*min-height: 100vh;\s*background: #fcfcfd;\s*\}', 
     '.main-content { margin-left: 280px; padding: 60px 80px; min-height: 100vh; background: #fcfcfd; }'),
    (r'\.filter-tab \{\s*display: inline-flex;\s*align-items: center;\s*height: 36px;\s*padding: 0 16px;\s*border-radius: 8px;\s*font-size: 14px;', 
     '.filter-tab { display: inline-flex; align-items: center; height: 48px; padding: 0 24px; border-radius: 10px; font-size: 16px;'),
    (r'\.search-bar input \{\s*height: 36px;\s*width: 220px;\s*padding: 0 12px 0 36px;\s*border: 1\.5px solid #e8e8e8;\s*border-radius: 8px;\s*font-size: 14px;', 
     '.search-bar input { height: 48px; width: 320px; padding: 0 16px 0 48px; border: 1.5px solid #e8e8e8; border-radius: 10px; font-size: 16px;'),
    (r'\.search-bar-icon \{\s*position: absolute;\s*left: 10px;\s*top: 50%;', 
     '.search-bar-icon { position: absolute; left: 16px; top: 50%; width: 20px; height: 20px;'),
    (r'\.project-card \{\s*background: #fff;\s*border: 1px solid #e8edf5;\s*border-radius: 14px;\s*overflow: hidden;\s*transition: all 0\.25s ease;\s*cursor: pointer;\s*\}', 
     '.project-card { background: #fff; border: 1px solid #e8edf5; border-radius: 16px; overflow: hidden; transition: all 0.25s ease; cursor: pointer; width: 410px; flex-shrink: 0; display: flex; flex-direction: column; }'),
    (r'\.project-card-header \{\s*background: #f9f9fb;\s*border-bottom: 1px solid #e8edf5;\s*padding: 9px 14px;\s*display: flex;\s*align-items: center;\s*gap: 6px;\s*font-size: 12px;', 
     '.project-card-header { background: #f9f9fb; border-bottom: 1px solid #e8edf5; padding: 18px 24px; display: flex; align-items: center; gap: 6px; font-size: 14px;'),
    (r'\.project-card-header \.yield-val \{\s*font-size: 13px;\s*font-weight: 700;', 
     '.project-card-header .yield-val { font-size: 16px; font-weight: 700;'),
    (r'\.project-card-img \{\s*position: relative;\s*height: 185px;\s*overflow: hidden;\s*\}', 
     '.project-card-img { position: relative; height: 268px; overflow: hidden; }'),
    (r'\.badge-active \{\s*position: absolute;\s*top: 10px;\s*right: 10px;\s*background: #661eb9;\s*color: #fff;\s*font-size: 11px;\s*font-weight: 600;\s*padding: 4px 10px;\s*border-radius: 5px;\s*\}', 
     '.badge-active { position: absolute; top: 16px; right: 16px; background: #661eb9; color: #fff; font-size: 14px; font-weight: 600; padding: 6px 14px; border-radius: 6px; }'),
    (r'\.badge-upcoming \{\s*position: absolute;\s*top: 10px;\s*right: 10px;\s*background: #f59e0b;\s*color: #fff;\s*font-size: 11px;\s*font-weight: 600;\s*padding: 4px 10px;\s*border-radius: 5px;\s*\}', 
     '.badge-upcoming { position: absolute; top: 16px; right: 16px; background: #f59e0b; color: #fff; font-size: 14px; font-weight: 600; padding: 6px 14px; border-radius: 6px; }'),
    (r'\.icon-btn \{\s*width: 36px;\s*height: 36px;\s*border: 1\.5px solid #e8e8e8;\s*border-radius: 8px;', 
     '.icon-btn { width: 48px; height: 48px; border: 1.5px solid #e8e8e8; border-radius: 10px;'),
    (r'\.progress-bar-bg \{\s*height: 5px;\s*width: 100%;\s*background: #e5e7eb;\s*border-radius: 99px;\s*overflow: hidden;\s*\}',
     '.progress-bar-bg { height: 6px; width: 100%; background: #e5e7eb; border-radius: 99px; overflow: hidden; }')
]

for old, new_s in css_updates:
    html = re.sub(old, new_s, html, flags=re.MULTILINE)

# 2. Update Header
html = html.replace('text-[28px] font-bold text-heading leading-tight mb-1', 'text-[48px] font-bold text-heading leading-tight mb-3 tracking-[-0.96px]')
html = html.replace('<p class="text-[14px] text-subtext leading-relaxed">', '<p class="text-[20px] text-body leading-relaxed max-w-[800px]">')
html = html.replace('<div class="mb-6">', '<div class="mb-[40px]">')
html = html.replace('gap-4 mb-7', 'gap-4 mb-[40px]')

# 3. Update Grid to Flex wrap
html = html.replace('<div class="grid grid-cols-3 gap-5" id="projectsGrid">', '<div class="flex flex-wrap gap-[30px]" id="projectsGrid" style="justify-content: flex-start;">')

# 4. Process all cards
card_pattern = re.compile(
    r'<div class="p-4 flex flex-col gap-3">\s*'
    r'<h3 class="text-\[15px\] font-semibold text-heading leading-snug">(.*?)</h3>\s*'
    r'<div class="flex justify-between items-center text-\[13px\] text-subtext">\s*'
    r'<span class="text-\[18px\] font-bold text-heading">(.*?)</span>\s*'
    r'<span>(.*?)</span>\s*'
    r'</div>\s*'
    r'<div class="progress-bar-bg">\s*'
    r'<div class="progress-bar-fill" style="(.*?)"></div>\s*'
    r'</div>\s*'
    r'<div class="flex justify-between text-\[12px\] text-subtext">\s*'
    r'<span>(.*?)</span>\s*'
    r'<span>(.*?)</span>\s*'
    r'</div>\s*'
    r'</div>'
)

def replace_card(m):
    title = m.group(1)
    amt = m.group(2)
    days = m.group(3)
    style = m.group(4)
    alloc = m.group(5)
    credits = m.group(6)
    
    return f'''<div class="p-[28px] flex flex-col gap-[28px] flex-grow">
          <h3 class="text-[22px] font-medium text-heading leading-[32px] min-h-[64px] tracking-tight">{title}</h3>
          <div class="flex flex-col gap-[20px] mt-auto">
            <div class="flex justify-between items-center w-full">
              <span class="text-[28px] font-semibold text-heading">{amt}</span>
              <span class="text-[18px] font-medium text-subtext">{days}</span>
            </div>
            <div class="flex flex-col gap-[15px]">
              <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="{style}"></div>
              </div>
              <div class="flex justify-between items-center text-[16px] font-medium text-subtext">
                <span class="text-heading font-medium">{alloc}</span>
                <span class="text-heading font-medium">{credits}</span>
              </div>
            </div>
          </div>
        </div>'''

html = card_pattern.sub(replace_card, html)

# 5. Fix logo size
html = html.replace('style="height:40px;', 'style="height:48px;')

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(html)
